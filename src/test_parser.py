import unittest
from parsers import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_text_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )


if __name__ == "__main__":
    unittest.main()