"""Strict UTF-8 artifacts. Markdown has one authoritative JSON fence."""
import hashlib
import json
import os
import re
import tempfile
import shutil
from pathlib import Path


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def read_artifact(path):
    path = Path(path)
    text = path.read_text(encoding='utf-8-sig')
    if path.suffix == '.md':
        blocks = re.findall(r'^```json\s*\n(.*?)^```\s*$', text, re.M | re.S)
        if len(blocks) != 1:
            raise ValueError(f'{path.name}: expected exactly one JSON block')
        text = blocks[0]
    result = json.loads(text, object_pairs_hook=unique_pairs,
                        parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))
    if not isinstance(result, dict):
        raise ValueError(f'{path.name}: artifact must be an object')
    return result


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_artifact(path, data, overwrite=False):
    path = Path(path)
    text = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    if path.suffix == '.md':
        text = f'# {path.stem}\n\nMachine contract; explanatory prose does not override this payload.\n\n```json\n{text}```\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    if not overwrite:
        with path.open('x', encoding='utf-8', newline='\n') as stream:
            stream.write(text)
        return
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.harness-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as stream:
            stream.write(text)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_artifacts_transaction(updates):
    """Stage all outputs; roll back a failed replacement, retaining recovery bytes
    if the OS also prevents rollback. Not a filesystem crash-atomic transaction.
    """
    paths = [Path(p).resolve() for p in updates]
    if not paths or len({p.parent for p in paths}) != 1:
        raise ValueError('transaction requires one artifact directory')
    parent = paths[0].parent
    stage = Path(tempfile.mkdtemp(dir=parent, prefix='.harness-transaction-'))
    committed = []
    recovered = True
    try:
        for destination, value in zip(paths, updates.values()):
            if not destination.is_file():
                raise FileNotFoundError(destination)
            (stage / (destination.name + '.backup')).write_bytes(destination.read_bytes())
            write_artifact(stage / destination.name, value)
        for destination in paths:
            os.replace(stage / destination.name, destination)
            committed.append(destination)
    except BaseException:
        for destination in reversed(committed):
            try:
                os.replace(stage / (destination.name + '.backup'), destination)
            except OSError:
                recovered = False
        if not recovered:
            raise OSError(f'rollback blocked by OS; recovery copies retained at {stage}')
        raise
    finally:
        if recovered and stage.resolve().is_relative_to(parent):
            shutil.rmtree(stage)
