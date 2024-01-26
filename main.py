import shutil, os, queue
from math import floor
from time import sleep, time_ns
from config import *
from readchar import readkey, key
from threading import Thread
#dont forgot to remove unused modules

text = ""
char = [None]
with open("allowed_chars.txt", "r") as file:
    for i in file:
        allowed_chars = i

def output(text):
    #gets terminal sizes
    x, y = shutil.get_terminal_size()
    doc_size = floor(x / 3) if floor(x / 3) >= min_width else min_width

    #raises exception if terminal 
    if x < min_width:
        raise(Exception("too_small_terminal_width"))
    
    br_strs = text.split("\n")
    spcs_strs = []
    for i in br_strs:
        if len(i) > doc_size - 2:
            str_i = i + " " * (doc_size - 2 - (len(i) // (doc_size - 2)))
        elif len(i) <= doc_size - 2:
            str_i = i + " " * (doc_size - 2 - len(i))
        spcs_strs.append(str_i)
    
    spcs_strs[-1] = br_strs[-1]
    text = "".join(spcs_strs)
    
    #blinking cursor timer
    cursor_timer = time_ns() // 1000000
    show_cursor = True

    if time_ns() // 1000000 - cursor_timer > 1000:
        cursor_timer = time_ns() // 1000000
        show_cursor = not(show_cursor)

    if show_cursor == True:
        text += "█"

    #spliting text for strings
    strs = [text[i:i + doc_size - 2] for i in range (0, len(text), doc_size-2)]
    if strs != []:
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

def render_call(text_queue):
    text = ""
    while True:
        try:
            text = text_queue.get(block = False, timeout = 0.05)
            print(output(text), end = "")
        except queue.Empty:
            pass

text_queue = queue.Queue()
renderer = Thread(target = render_call, args = (text_queue,), daemon = True)
renderer.start()
#text_queue.get()
while True:
    text_queue.put(text, block = False, timeout = 0.05)
    getchar = readkey()

    if getchar in allowed_chars:
        text += getchar  

    match getchar:
        case key.BACKSPACE:
            text = text[:-1]
        case key.ENTER:
            text += "\n"
        case key.TAB:
            text += "    "
