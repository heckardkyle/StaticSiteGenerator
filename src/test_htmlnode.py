import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        string = ""
        self.assertEqual(string, node.props_to_html())
    
    def test_props_to_html2(self):
        dict = {}
        dict["key"] = "value"
        node = HTMLNode(props=dict)
        string = 'key="value"'
        self.assertEqual(string, node.props_to_html())

    def test_props_to_html3(self):
        dict = {}
        node = HTMLNode(props=dict)
        string = ""
        self.assertEqual(string, node.props_to_html())

    def test_props_to_html4(self):
        dict = {}
        dict["key1"] = "value1"
        dict["key2"] = "value2"
        node = HTMLNode(props=dict)
        string = 'key1="value1" key2="value2"'
        self.assertEqual(string, node.props_to_html())

    def test_props_to_html5(self):
        dict = {}
        dict["key1"] = "value1"
        dict["key2"] = "value2"
        dict["key3"] = "value3"
        node = HTMLNode(props=dict)
        string = 'key1="value1" key2="value2" key3="value3"'
        self.assertEqual(string, node.props_to_html())
        
    def test_props_to_html6(self):
        node = HTMLNode(props=None)
        string = ""
        self.assertEqual(string, node.props_to_html())

    def test_LeafNode_props_to_html(self):
        dict = {}
        dict["key1"] = "value1"
        dict["key2"] = "value2"
        node = LeafNode("p", "value", dict)
        string = 'key1="value1" key2="value2"'
        self.assertEqual(string, node.props_to_html())

    def test_LeafNode(self):
        node = LeafNode(None, "value")
        string = "value"
        self.assertEqual(string, node.to_html())

    def test_LeafNode2(self):
        node = LeafNode(None, "value", {"k": "v"})
        string = "value"
        self.assertEqual(string, node.to_html())

    def test_LeafNode3(self):
        node = LeafNode("p", "value")
        string = "<p>value</p>"
        self.assertEqual(string, node.to_html())

    def test_LeafNode4(self):
        node = LeafNode("a", "value", {"k1": "v1", "k2": "v2"})
        string = '<a k1="v1" k2="v2">value</a>'
        self.assertEqual(string, node.to_html())


if __name__ == "__main__":
    unittest.main()