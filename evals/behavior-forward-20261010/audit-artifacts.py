"""Read-only integrity audit of the isolated forward-test artifacts."""
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / '.local/behavior-forward-20261010'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

frozen = read(ROOT / 'frozen-input-manifest.json')
evaluation = Path(__file__).resolve().parent
freeze = read(evaluation / 'freeze.json')
freeze_errors = [name for name, actual, expected in [
    ('protocol', sha(evaluation / 'PROTOCOL.md'), freeze['protocol_sha256']),
    ('local frozen manifest', sha(ROOT / 'frozen-input-manifest.json'), freeze['input_manifest_sha256']),
    ('saved frozen manifest', sha(evaluation / 'frozen-input-manifest.json'), freeze['input_manifest_sha256']),
] if actual != expected]
protected = {name: digest for name, digest in frozen.items()
             if name.startswith(('package/', 'reference/'))
             or '/reference/' in name
             or name.endswith(('/PRODUCT.md', '/REQUEST.md', '/AGENTS.md'))}
changed = [name for name, digest in protected.items()
           if not (ROOT / name).is_file() or sha(ROOT / name) != digest]
package = ROOT / 'package/joedesign'
def package_files(directory):
    return {path.relative_to(directory).as_posix(): sha(path)
            for path in directory.rglob('*') if path.is_file()
            and path.suffix != '.pyc' and '__pycache__' not in path.parts}

pinned_files = package_files(package)
source_files = package_files(REPO / 'skills/joedesign')
source_changes = sorted(name for name in pinned_files.keys() | source_files.keys()
                        if pinned_files.get(name) != source_files.get(name))
frames = []
for path in (ROOT / 'cases').rglob('*.json'):
    try:
        data = read(path)
    except (ValueError, UnicodeError):
        continue
    if not isinstance(data, dict) or 'frame_hashes' not in data:
        continue
    recorded_errors = [name for name, digest in data['frame_hashes'].items()
                       if not Path(name).is_file() or sha(Path(name)) != digest]
    archived = ROOT / 'cases/extension/evidence/proof-attempt1'
    relocations = []
    errors = recorded_errors
    if path.is_relative_to(archived):
        # Explicit archive only: verify preserved bytes without editing or rebinding
        # the original failed observation to today's files at its former location.
        relocations = [{'recorded_path': name, 'archive_path': str(path.parent / Path(name).name),
                        'hash_matches': (path.parent / Path(name).name).is_file()
                        and sha(path.parent / Path(name).name) == digest}
                       for name, digest in data['frame_hashes'].items()]
        errors = [row['archive_path'] for row in relocations if not row['hash_matches']]
    frames.append({'observation': str(path.relative_to(ROOT)), 'changed_frames': errors,
                   'recorded_path_mismatches': recorded_errors, 'archive_relocations': relocations})

report = {'freeze_errors': freeze_errors,
          'protected_files_checked': len(protected), 'changed_protected_inputs': changed,
          'pinned_package_files': len(pinned_files), 'source_package_files': len(source_files),
          'source_vs_pinned_package_changes': source_changes,
          'observation_frame_integrity': frames,
          'limitations': 'Byte integrity only; does not authenticate observations or visual judgment.'}
print(json.dumps(report, indent=2))
raise SystemExit(bool(freeze_errors or changed or source_changes or any(row['changed_frames'] for row in frames)))
