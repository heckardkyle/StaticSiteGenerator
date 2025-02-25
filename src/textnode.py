from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode):
        if self.text != TextNode.text:
            return False
        if self.text_type.value != TextNode.text_type.value:
            return False
        if self.url != TextNode.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode("code", text_node.text)
        case (TextType.LINK):
            return LeafNode("a", text_node.text, text_node.url)
        case (TextType.IMAGE):
            props = dict(text_node.url)
            props["alt"] = text_node.text
            return LeafNode("img", "", props)
        case _:
            raise Exception("Text Type not valid")