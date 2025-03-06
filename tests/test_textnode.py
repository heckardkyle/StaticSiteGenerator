import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
    
    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Node4", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "something")
        self.assertNotEqual(node, node2)

    def test_eq6(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Node7", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq7(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Node8", TextType.BOLD, "something")
        self.assertNotEqual(node, node2)

    def test_eq8(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC, "something")
        self.assertNotEqual(node, node2)

    def test_eq9(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node10 = TextNode("node10", TextType.ITALIC, "something")
        self.assertNotEqual(node, node10)
    
    def test_text_to_html_node_text(self):
        text_node = TextNode("some text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "some text"
        assert html_node.props == None

    def test_text_to_html_node_bold(self):
        text_node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == ""
        assert html_node.props == None
    
    def test_text_to_html_node_italic(self):
        text_node = TextNode("some text", TextType.ITALIC, {"a": "b"})
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "i"
        assert html_node.value == "some text"
        assert html_node.props == None

    def test_text_to_html_node_code(self):
        text_node = TextNode("!  code  text  !", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "code"
        assert html_node.value == "!  code  text  !"
        assert html_node.props == None

    def test_text_to_html_node_link(self):
        props = {"href": "places"}
        text_node = TextNode("some text", TextType.LINK, props)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "some text"
        self.assertEqual(html_node.props, props)

    def test_text_to_html_node_image(self):
        props = {"src": "url", "alt": "caption"}
        text_node = TextNode("caption", TextType.IMAGE, props)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        self.assertEqual(html_node.props, props)

    def test_text_to_html_node_invalid(self):
        invalid_text_node = TextNode("caption", "not valid")
        with self.assertRaises(Exception):
            text_node_to_html_node(invalid_text_node)
    


if __name__ == "__main__":
    unittest.main()