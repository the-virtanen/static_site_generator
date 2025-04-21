class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_output =""
        props = self.props
        for prop in props:
            html_output += f' {prop}:"{props[prop]}"'
    
        return html_output
    
    def __repr__(self):
        return (
            f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):        
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        value = self.value
        
        if value == None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag == None:
            return self.value
        
        tag = self.tag.lower()
        return f"<{tag}>{value}</{tag}>"
    
    def __repr__(self):
        return (
            f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}"
        )

