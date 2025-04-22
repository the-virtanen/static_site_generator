from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    text = text_node.text
    url = text_node.url

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text)
        case TextType.BOLD:
            return LeafNode("b", text)
        case TextType.ITALIC:
            return LeafNode("i", text)
        case TextType.CODE:
            return LeafNode("code", text)
        case TextType.LINK:
            return LeafNode("a", text, {"href": url})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src": url, "alt": url})
        case _:
            return("Incorrect text type")
          
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        blocks = text.split(delimiter)
        if len(blocks) % 2 == 0:
            raise Exception("invalid markdown syntax")
        
        for i in range(len(blocks)):
            if i % 2 == 0:
                if blocks[i] == "":
                    continue
                new_nodes.append(TextNode(blocks[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(blocks[i], text_type))

    return new_nodes


if __name__ == "__main__":
    node = TextNode("This is **bold text** with a **super bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)

          
          
          