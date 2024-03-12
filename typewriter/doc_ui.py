import shutil
from math import floor
from threading import Thread
from configs.config import *

class Doc_UI():
    def __init__(self):
        self.text = ""

    def doc_output(self, text_data):
        """Function, which displays document in the terminal\n
        Using:
        >>> doc_output(add_text)
        """

        from readchar import key
        from os import system

        got_text = text_data.get_data()
        match got_text:
            case key.BACKSPACE:
                self.text = self.text[:-1]
                text_data.set_data("")
            case _:
                self.text = self.text + got_text

        #do_exec = True
        #try:
        #    if self.text == text_copy:
        #        do_exec = False
        #except:
        #    do_exec = False
        
        text = self.text
        #text_copy = self.text

        #gets terminal sizes, sets width of doc
        x, y = shutil.get_terminal_size()
        doc_size = floor(x / (100 / width_percent)) if floor(x / (100 / width_percent)) >= min_width else min_width
        
        #breaklines realisation
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
        
        #cursor
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
                " " * int((x - doc_size) / 2) + "┗" + "━" * (doc_size - 2) + "┛" + " " * int((x - doc_size) / 2) + " " * first_line_shift
        
        #raises exception if terminal too narrow
        if x < min_width:
            text = f"Your terminal is too small. (width < {min_width})"
        
        #if do_exec:
        return output

if __name__ == "__main__":
    print("You are running a wrong file. Try run main.py.")
    