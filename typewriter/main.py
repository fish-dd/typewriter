import queue
from configs.config import *
from threading import Thread
from key_input import input_handler
from doc_ui import Doc_UI

doc1 = Doc_UI()
text_queue = queue.Queue()

def render_call(text_queue, doc1):
    while True:
        try:
            text = text_queue.get(block = False, timeout = 0.05)
            print(doc1.doc_output(text), end = "")
        except queue.Empty:
            pass

renderer = Thread(target = render_call, args = (text_queue, doc1), daemon = True)
renderer.start()