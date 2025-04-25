from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE ="code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    
    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    rows = block.split("\n")

    if rows[0][0] == ">":
        is_quote = True
        for row in rows:
            if row[0] != ">":
                is_quote = False
                break
        
        if is_quote:
            return BlockType.QUOTE

    if rows[0][0:2] == "- ":
        is_unordered_list = True
        for row in rows:
            if row[0:2] != "- ":
                is_unordered_list = False
                break
        
        if is_unordered_list:
            return BlockType.UNORDERED_LIST


    if rows[0][0:2] == "- ":
        is_unordered_list = True
        for row in rows:
            if row[0:2] != "- ":
                is_unordered_list = False
                break
        
        if is_unordered_list:
            return BlockType.UNORDERED_LIST
    
    #is_ordered_list == True
    for row in rows:
        check_row = row.split(". ", 1)
        print(check_row)
        #rows_start_with_number = re.findall(r"\b(\d+)\. ", row)


    return BlockType.PARAGRAPH

    
    
    


if __name__ == "__main__":
    block = "- what \n-is this\n- stuff"
    print(block_to_block_type(block))

    text = """1. sdf
2. 21345
3. ölkjasdf
4. alöksj
5. b
6. l
7. asd
8. as
9. asdf
10. hello"""

    print(block_to_block_type(text))