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
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return (
            f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}"
        )

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode tag missing")
        if self.children == None:
            raise ValueError("Children missing from parent")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
  
    def __repr__(self):
        return (
            f"tag: {self.tag}\nchildren: {self.children}\nprops: {self.props}"
        )


if __name__ == "__main__":
    print("moi :)")