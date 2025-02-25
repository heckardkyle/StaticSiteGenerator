from textnode import TextType, TextNode

def main():
    node = TextNode("sometext", TextType.BOLD, "url")
    print(node)

main()