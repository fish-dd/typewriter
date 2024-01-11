import shutil
from math import floor
from time import sleep

x, y = shutil.get_terminal_size()
doc_size = floor(x / 3) if floor(x / 3) >= 60 else 60

output = " " * int((x - doc_size) / 2) + "┏" + "━" * (doc_size - 2) + "┓" + " " * int((x - doc_size) / 2) + "\n" + \
        (" " * int((x - doc_size) / 2) + "┃" + " " * (doc_size - 2) + "┃" + " " * int((x - doc_size) / 2) + "\n") * (y - 2) + \
         " " * int((x - doc_size) / 2) + "┗" + "━" * (doc_size - 2) + "┛" + " " * int((x - doc_size) / 2)

while True:
    print(output, end = "")
    sleep(0.05)