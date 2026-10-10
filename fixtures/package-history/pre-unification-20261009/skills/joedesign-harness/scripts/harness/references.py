"""Read OMD documents as data, never execute their workflows or infer observations."""
import re
from pathlib import Path
from .io import digest, file_hash


def build_index(root):
    root = Path(root).resolve(strict=True)
    records = []
    seen = set()
    for path in sorted(root.rglob('DESIGN.md')):
        resolved = path.resolve(strict=True)
        if not resolved.is_relative_to(root):
            raise ValueError('reference symlink escapes catalog root')
        if path.stat().st_size > 2_000_000:
            raise ValueError(f'reference too large: {path}')
        text = path.read_text(encoding='utf-8-sig')
        match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
        fields = {}
        if match:
            # Deliberately support only scalar top-level metadata. Nested YAML and
            # evidence claims remain in the original document, not recovered facts.
            for key, value in re.findall(r'^([\w-]+):[ \t]*([^\n]*)$', match[1], re.M):
                if key in fields:
                    raise ValueError(f'duplicate metadata key: {key}')
                fields[key] = value.strip().strip('\"\'')
        source_id = fields.get('id') or path.parent.name
        if source_id in seen:
            raise ValueError(f'duplicate reference id: {source_id}')
        seen.add(source_id)
        records.append({'id': source_id, 'name': fields.get('name', source_id),
                        'category': fields.get('category') or 'UNKNOWN',
                        'quality': fields.get('quality_status') or fields.get('quality') or 'UNKNOWN',
                        'homepage': fields.get('homepage') or 'UNKNOWN',
                        'path': str(resolved), 'sha256': file_hash(path),
                        'inspection': 'VISUAL_UNINSPECTED', 'search_text': text.casefold()})
    if not records:
        raise ValueError('no reference DESIGN.md documents found')
    return {'schema_version': 1, 'root': str(root), 'references': records,
            'fingerprint': digest([{'id': r['id'], 'sha256': r['sha256']} for r in records])}


def retrieve(index, intent, limit=10):
    terms = intent.get('search_terms', [])
    if not isinstance(terms, list) or not terms or any(not isinstance(t, str) or not t.strip() for t in terms):
        raise ValueError('nonempty explicit search_terms required')
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError('limit must be 1..100; expand deliberately when needed')
    filters = intent.get('reference_filters', {})
    ranked = []
    for item in index['references']:
        if any(item.get(key, 'UNKNOWN') not in allowed for key, allowed in filters.items()):
            continue
        matches = [t for t in terms if t.casefold() in item['search_text']]
        if matches:
            output = {k: v for k, v in item.items() if k != 'search_text'}
            output.update(matched_terms=matches, fit='UNVERIFIED',
                          unresolved_requirements=[r['id'] for r in intent.get('requirements', [])])
            ranked.append(output)
    ranked.sort(key=lambda item: (-len(item['matched_terms']), item['id']))
    return {key: intent.get(key) for key in ('candidate_id', 'revision', 'scope_id')} | {
        'catalog_fingerprint': index['fingerprint'], 'candidates': ranked[:limit],
        'status': 'SHORTLIST_ONLY' if ranked else 'REFERENCE_INSUFFICIENT',
        'selection_rule': 'Term overlap locates documents; actual visual/structural fit requires inspection.'}
