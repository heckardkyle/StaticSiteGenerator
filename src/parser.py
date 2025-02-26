from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        elif node.text.count(delimiter) != 2:
            raise Exception("There must be 2 delimiters")
        else:
            parsed_text = node.text.split(delimiter)
            nodes.append(TextNode(parsed_text[0], node.text_type))
            nodes.append(TextNode(parsed_text[1], text_type))
            nodes.append(TextNode(parsed_text[2], node.text_type))

    return nodes