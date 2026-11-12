#!/usr/bin/env python3
'''Read-only static resource inventory for the Masters Union Nations site.'''
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MEDIA_EXTS = {'.mp3', '.wav', '.mp4', '.webm', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg'}

def inventory(root=ROOT):
    records=[]
    for path in root.rglob('*'):
        if not path.is_file() or '.git' in path.parts: continue
        if path.suffix.lower() not in MEDIA_EXTS: continue
        records.append({'path':path.relative_to(root).as_posix(),'bytes':path.stat().st_size})
    return sorted(records,key=lambda x:x['bytes'],reverse=True)

def source_paths(index_html):
    # Accept both root-relative asset paths and explicit ./assets paths.
    paths = re.findall(r'''(?:src|href)=["'](?:[.]/)?(assets/[^"'?#]+)''', index_html)
    return set(paths)

def oversized_media(root=ROOT, max_bytes=10 * 1024 * 1024):
    """Return large local media records for performance planning."""
    if max_bytes < 1:
        raise ValueError("max_bytes must be positive")
    return [item for item in inventory(root) if item['bytes'] > max_bytes]

if __name__=='__main__':
    index=(ROOT/'index.html').read_text()
    refs=source_paths(index)
    missing=sorted(ref for ref in refs if not (ROOT/ref).exists())
    data={'media_files':len(inventory()),'largest_media_files':inventory()[:10],
          'direct_resource_references':len(refs),'missing_direct_resources':missing, 'media_over_10mb':oversized_media(ROOT)}
    print(json.dumps(data,indent=2))
    # The independent public edition intentionally excludes unverified audio media.
    # Report, but do not fail solely because those music files were omitted.
    other_missing=[x for x in missing if not x.startswith('assets/audio/')]
    if other_missing: raise SystemExit('Non-audio resources are missing')
