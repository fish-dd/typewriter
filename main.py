import shutil
from math import floor
from time import sleep
from config import *

def output(text):
    #gets terminal sizes
    x, y = shutil.get_terminal_size()
    doc_size = floor(x / 3) if floor(x / 3) >= 60 else 60

    #raises exception if terminal 
    if x < min_width:
        raise(Exception("too_small_terminal_width"))

    #spliting text for strings
    strs = [text[i:i + doc_size - 2] for i in range (0, len(text), doc_size-2)]
    strs[-1] = strs[-1] + " " * ((doc_size - 2) - len(strs[-1]))
    for i in range(y - 2 - len(strs)):
        strs.append(" " * (doc_size - 2))

    #text area of the document
    text_area = ""
    for i in range(y - 2):
        text_area += " " * int((x - doc_size) / 2) + "┃" + strs[i] + "┃" + " " * int((x - doc_size) / 2) + "\n"
    
    #final output
    output = " " * int((x - doc_size) / 2) + "┏" + "━" * (doc_size - 2) + "┓" + " " * int((x - doc_size) / 2) + "\n" + \
            text_area + \
            " " * int((x - doc_size) / 2) + "┗" + "━" * (doc_size - 2) + "┛" + " " * int((x - doc_size) / 2)\
    
    return output

while True:
    print(output(text), end = "")
    sleep(0.1)