import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestHTMLNode(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "# header"
        blocktype = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(blocktype, expected)

    def test_block_to_block_type_code(self):
        block = "``` code"
        blocktype = block_to_block_type(block)
        expected = BlockType.CODE
        self.assertEqual(blocktype, expected)
    
    def test_block_to_block_type_quote(self):
        block = "> quote"
        blocktype = block_to_block_type(block)
        expected = BlockType.QUOTE
        self.assertEqual(blocktype, expected)

    def test_block_to_block_type_unordered_list(self):
        block = "- unordered list"
        blocktype = block_to_block_type(block)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(blocktype, expected)
    
    def test_block_to_block_type_ordered_list(self):
        block = "23. ordered list"
        blocktype = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(blocktype, expected)

    def test_block_to_block_type_paragraph(self):
        block = "23.ordered list"
        blocktype = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(blocktype, expected)