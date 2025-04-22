from textnode import *
from htmlnode import *


def main():
    t1 = TextNode("hello", TextType.IMAGE, "https://www.boot.dev")
    h1 = HTMLNode( props={"href": "https://www.google.com","target": "_blank",})

    print(t1)
    print(h1)
  

main()