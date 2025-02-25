

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        if self.props == None:
            return string
        for prop in self.props:
            string += f'{prop}="{self.props[prop]}" '
        return string[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("A leaf node must have a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Node requires a tag")
        if self.children == None:
            raise ValueError("Parent Node requires children")
        child_string = ""
        for child in self.children:
            child_string += child.to_html()
        if self.props == None:
            return f"<{self.tag}>{child_string}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{child_string}</{self.tag}>"