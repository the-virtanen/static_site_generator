from text_function import *
from text_function import *

def text_to_textnodes(text):
    text_list = [TextNode(text, TextType.TEXT),]

    text_list = split_nodes_delimiter(text_list, "**", TextType.BOLD)
    text_list = split_nodes_delimiter(text_list, "_", TextType.ITALIC)
    text_list = split_nodes_delimiter(text_list, "`", TextType.CODE) ##siirrä tää jos tulee bugi koodinoden sisällä

    text_list = split_nodes_image(text_list)
    
    text_list = split_nodes_link(text_list)
    return text_list


if __name__ == "__main__":
    print(text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))