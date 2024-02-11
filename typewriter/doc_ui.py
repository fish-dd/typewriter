class Doc_UI():
    import shutil
    from math import floor
    from threading import Thread
    from configs.config import min_width
    def __init__(self):
        pass

    def doc_output(self, text):
        """Function, which displays document in the terminal\n
        Using:
        >>> doc_output(text = text)
        """
        min_width = self.min_width
        shutil = self.shutil
        floor = self.floor
        text = self.text

        #gets terminal sizes
        x, y = shutil.get_terminal_size()
        doc_size = floor(x / 2.5) if floor(x / 2.5) >= min_width else min_width

        #raises exception if terminal too narrow
        if x < min_width:
            raise(Exception("too_small_terminal_width"))
        
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
                " " * int((x - doc_size) / 2) + "┗" + "━" * (doc_size - 2) + "┛" + " " * int((x - doc_size) / 2)\
        
        return output


    