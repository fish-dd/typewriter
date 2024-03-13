def input_handler(allowed_chars, text_queue):
    """Handle the key presses"""
    from readchar import readkey, key

    while True:
        getchar = readkey()

        if getchar in allowed_chars:
            text = getchar  

        match getchar:
            case key.BACKSPACE:
                text = "code_bckspce"
            case key.ENTER:
                text = "\n"
            case key.TAB:
                text = "    "

        text_queue.put(text, block = False, timeout = 0.05)

if __name__ == "__main__":
    print("You are running a wrong file. Try run main.py.")
