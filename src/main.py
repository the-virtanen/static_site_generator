from textnode import *
from htmlnode import HTMLNode

def main():
    t1 = TextNode("hello", TextType.LINK, "https://www.boot.dev")
    h1 = HTMLNode( props={"href": "https://www.google.com","target": "_blank",})
    print(h1)

main()