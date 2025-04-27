from htmlnode import *
from textnode import *
from text_to_textnode import *
from blocktype import *
from block_markdown import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_list = []
    for block in blocks:
       
        block_list.append(create_html_node(block))

    return ParentNode("div", block_list)


def create_html_node(block):
    block_type = block_to_block_type(block)
    
    match block_type:
        case BlockType.PARAGRAPH:
            children = text_nodes_to_leaf(block)

            return ParentNode("p", children)
        
def text_nodes_to_leaf(text):
    text_list = text_to_textnodes(text)
    leaf_nodes = []
    for text in text_list:
        if text.text_type == TextType.TEXT:
            leaf_nodes.append(LeafNode(None,text.text))
        if text.text_type == TextType.ITALIC:
            leaf_nodes.append(LeafNode("i",text.text))
        if text.text_type == TextType.BOLD:
            leaf_nodes.append(LeafNode("b",text.text))

    return leaf_nodes



if __name__ == "__main__":
    md="""
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_html_node(md)
    #print(node)
    html = node.to_html()

    print(html)
    #"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"