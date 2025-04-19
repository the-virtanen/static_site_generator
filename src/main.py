from textnode import *

t1 = TextNode("hello", "text")
t2 = TextNode("fuck","link","www.derp.com")

print(repr(t1))
print(repr(t2))
print(t1 = t2)