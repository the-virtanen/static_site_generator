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
          