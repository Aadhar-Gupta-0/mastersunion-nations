import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
from site_audit import source_paths

class SiteAuditTests(unittest.TestCase):
    def test_asset_references(self):
        self.assertEqual(source_paths('<img src="assets/a.webp"><link href="assets/b.css?v=1">'), {'assets/a.webp','assets/b.css'})
    def test_external_urls_ignored(self):
        self.assertEqual(source_paths('<script src="https://example.com/script.js"></script>'),set())

if __name__=='__main__': unittest.main()
