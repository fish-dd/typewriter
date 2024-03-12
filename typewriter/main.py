import queue
from configs.config import *
from threading import Thread
from key_input import input_handler
from doc_ui import Doc_UI
from time import sleep
import os

class data_class():
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data

doc1 = Doc_UI()
text_queue = queue.Queue()
text_data = data_class()

def render_call(doc1, text_data):
    while True:
        try:
            text = text_queue.get(block = False, timeout = 0.05)
        except:
            text = ""
        text_data.set_data(text)
        print(doc1.doc_output(text_data), end = "")
        sleep(0.01)

if __name__ == "__main__":
    os.system(clear_command)
    renderer = Thread(target = render_call, args = (doc1, text_data), daemon = True)
    renderer.start()
    try:
        input_handler(allowed_chars, text_queue)
    except KeyboardInterrupt:
        os.system(clear_command)
        print("typewriter α", end = "")
