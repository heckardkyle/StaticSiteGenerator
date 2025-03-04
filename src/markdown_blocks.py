from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    if block[0:3] == "```":
        return BlockType.CODE
    if block[0] == ">":
        return BlockType.QUOTE
    if block[0:2] == "- ":
        return BlockType.UNORDERED_LIST
    match = re.match(r"^\d+\. ", block)
    if match:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block != "":
            new_blocks.append(block.strip())

    return new_blocks