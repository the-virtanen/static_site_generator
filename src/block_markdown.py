def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        
        if block == "":
            continue
        
        block = block.strip()
        clean_blocks.append(block)
    
    return clean_blocks

md = """

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
blocks = markdown_to_blocks(md)
print(blocks)
