"""Strict UTF-8 artifacts. Markdown has one authoritative JSON fence."""
import hashlib
import json
import os
import re
import tempfile
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
