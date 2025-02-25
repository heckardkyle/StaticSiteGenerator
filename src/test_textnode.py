import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()