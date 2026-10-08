import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import dorkgen  # noqa: E402


class LibraryTests(unittest.TestCase):
    def test_library_valid(self):
        self.assertGreater(len(dorkgen.load_library()), 10)

    def test_all_templates_scoped(self):
        for d in dorkgen.load_library():
            self.assertIn("{domain}", d["template"], d["id"])


class DomainTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(dorkgen.validate_domain("Example.COM"), "example.com")

    def test_invalid(self):
        for bad in ["", "localhost", "exa mple.com", "http://example.com", "a..b.com", "-x.com"]:
            with self.assertRaises(ValueError, msg=bad):
                dorkgen.validate_domain(bad)


class CliTests(unittest.TestCase):
    def test_requires_authorized(self):
        self.assertEqual(dorkgen.main(["generate", "-d", "example.com"]), 2)

    def test_generate_ok(self):
        self.assertEqual(dorkgen.main(["generate", "-d", "example.com", "--authorized"]), 0)

    def test_filter_category(self):
        items = dorkgen.select(dorkgen.load_library(), category="documents")
        self.assertTrue(items and all(d["category"] == "documents" for d in items))

    def test_url_encoding(self):
        self.assertIn("q=site%3Aexample.com", dorkgen.search_url("site:example.com"))


if __name__ == "__main__":
    unittest.main()
