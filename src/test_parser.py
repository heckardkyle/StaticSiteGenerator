import unittest
from parsers import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestParser(unittest.TestCase):
    def test_split_nodes_delimiter_no_parse(self):
        node = TextNode("Bold text", TextType.BOLD)
        old_nodes = [
            node
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("Bold text", TextType.BOLD)
        ]
        self.assertEqual(expected_nodes, new_nodes)

    def test_split_nodes_delimiter_bold_parse(self):
        node = TextNode("Text with **Bold** stuff", TextType.TEXT)
        old_nodes = [
            node
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("Bold", TextType.BOLD),
            TextNode(" stuff", TextType.TEXT)
        ]
        self.assertEqual(expected_nodes, new_nodes)

    def test_split_nodes_delimiter_italic_parse(self):
        node = TextNode("Text with _italic_ stuff", TextType.TEXT)
        old_nodes = [
            node
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" stuff", TextType.TEXT)
        ]
        self.assertEqual(expected_nodes, new_nodes)

    def test_split_nodes_delimiter_two_parse_bold(self):
        node = TextNode("Text with **Bold** stuff", TextType.TEXT)
        node2 = TextNode("Text with **Bold** stuff", TextType.TEXT)
        old_nodes = [
            node,
            node2
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("Bold", TextType.BOLD),
            TextNode(" stuff", TextType.TEXT),
            TextNode("Text with ", TextType.TEXT),
            TextNode("Bold", TextType.BOLD),
            TextNode(" stuff", TextType.TEXT)
        ]
        self.assertEqual(expected_nodes, new_nodes)

    def test_split_nodes_delimiter_exception1(self):
        node = TextNode("Text with **Bold stuff", TextType.TEXT)
        old_nodes = [
            node
        ]
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    def test_split_nodes_delimiter_exception2(self):
        node = TextNode("Text with **Bold**** stuff", TextType.TEXT)
        old_nodes = [
            node
        ]
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    def test_extract_markdown_images(self):
        text = "Some text ![image](htp#!a) and ![af](asfkdl)"
        matches = extract_markdown_images(text)
        expected = [
            ("image", "htp#!a"),
            ("af", "asfkdl")
        ]
        self.assertEqual(matches, expected)

    def test_extract_markdown_links(self):
        text = "Text with [one link](link) and [another](lsfine.cs)"
        matches = extract_markdown_links(text)
        expected = [
            ("one link", "link"),
            ("another", "lsfine.cs")
        ]
        self.assertEqual(matches, expected)


if __name__ == "__main__":
    unittest.main()