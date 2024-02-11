def input_handler(allowed_chars, text, text_queue):
    """Handle the key presses"""
    from readchar import readkey, key

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
        