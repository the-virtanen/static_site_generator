from textnode import *
from htmlnode import *
from extracts import *

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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)

        if images == None:
            new_nodes.append(node)
            continue

        replaced_text = text
        for imgage_alt, image_url in images:
            image_node = TextNode(imgage_alt, TextType.IMAGE, image_url)
            replaced_text = text.replace(f"![{imgage_alt}]({image_url})", f"||{image_node}||") ## returns sting need to fix
            sections = replaced_text.split("||")
            new_nodes.extend( sections )            
            

        """
        if len(blocks) % 2 == 0:
            raise Exception("invalid markdown syntax")
        
        for i in range(len(blocks)):
            if i % 2 == 0:
                if blocks[i] == "":
                    continue
                new_nodes.append(TextNode(blocks[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(blocks[i], text_type))
        """
    return new_nodes
    #return new_nodes

if __name__ == "__main__":
    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
    new_nodes = split_nodes_image([node])
    print(new_nodes)

          
          
          