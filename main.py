import shutil, os, queue
from math import floor
from time import sleep
from config import *
from readchar import readkey, key
from threading import Thread
#dont forgot to remove unused modules

text = ""
char = [None]
allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 */-+=_'\"[]{}|!@#$%^&*()?.<>,~`"

def output(text):
    #gets terminal sizes
    x, y = shutil.get_terminal_size()
    doc_size = floor(x / 3) if floor(x / 3) >= 60 else 60

    #raises exception if terminal 
    if x < min_width:
        raise(Exception("too_small_terminal_width"))

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

def render_config(text_queue):
    text = ""
    while True:
        try:
            text = text_queue.get()
            print(output(text), end = "")
            sleep(0.05)
        except queue.Empty:
            pass

text_queue = queue.Queue()
renderer = Thread(target = render_config, args = (text_queue,), daemon = True)
renderer.start()
while True:
    getchar = readkey()
    if getchar == None:
        pass
    elif getchar in allowed_chars:
        text += getchar
    elif getchar == key.BACKSPACE:
        text = text[:-1]
    text_queue.put(text)
