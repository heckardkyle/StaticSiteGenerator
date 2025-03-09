import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or node.text.count(delimiter) <= 0:
            nodes.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise Exception("There must be 2 delimiters")
        else:
            parsed_text = node.text.split(delimiter)
            for text in parsed_text:
                if parsed_text.index(text) % 2 == 0:
                    nodes.append(TextNode(text, TextType.TEXT))
                else:
                    nodes.append(TextNode(text, text_type))

    return nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
            text = node.text
            while True:  # Process all images iteratively
                extracted_images = extract_markdown_images(text)
                if not extracted_images:
                    # If no more images, append the remaining text as TextNode
                    if text:  # Only add if there is remaining text
                        nodes.append(TextNode(text, node.text_type))
                    break
                
                # Extract the first image from the list
                extract = extracted_images[0]
                split_text = text.split(f"![{extract[0]}]({extract[1]})", 1)
                
                # Append everything before the image
                if split_text[0]:
                    nodes.append(TextNode(split_text[0], node.text_type))
                
                # Append the image as a node
                nodes.append(TextNode(extract[0], TextType.IMAGE, extract[1]))
                
                # Update `text` to the remainder after the image
                text = split_text[1] if len(split_text) > 1 else ""

    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
            text = node.text
            while True:  # Process all images iteratively
                extracted_links = extract_markdown_links(text)
                if not extracted_links:
                    # If no more images, append the remaining text as TextNode
                    if text:  # Only add if there is remaining text
                        nodes.append(TextNode(text, node.text_type))
                    break
                
                # Extract the first image from the list
                extract = extracted_links[0]
                split_text = text.split(f"[{extract[0]}]({extract[1]})", 1)
                
                # Append everything before the image
                if split_text[0]:
                    nodes.append(TextNode(split_text[0], node.text_type))
                
                # Append the image as a node
                nodes.append(TextNode(extract[0], TextType.LINK, extract[1]))
                
                # Update `text` to the remainder after the image
                text = split_text[1] if len(split_text) > 1 else ""

    return nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
