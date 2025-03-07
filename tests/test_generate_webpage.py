import unittest
from generate_webpage import extract_title

class TestGenerateWebpage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# title  \n"
        expected = "title"
        self.assertEqual(expected, extract_title(markdown))

    def test_extract_title_h2(self):
        markdown = "## title"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_no_h(self):
        markdown = "title"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_multiple_lines(self):
        markdown = "# title \n second line"
        expected = "title"
        self.assertEqual(expected, extract_title(markdown))