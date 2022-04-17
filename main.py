import tkinter as tk
import link



def encoding(byt, encoding):
    try:
        return byt.get().encode("UTF-8").decode(encoding)
    except UnicodeDecodeError:
        return "Decode Error"


def codepoint(byt):
    return hex(ord(byt.get()[0]))[2:]


class State:
    def __init__(self) -> None:
        try:
            self.raw_clipboard = root.clipboard_get().encode("UTF-8")
        except:  # happens when there's no clipboard set
            self.raw_clipboard = b""
        self.string_encoding = "UTF-8"
        self.clipboard = self.raw_clipboard.decode(self.string_encoding)
        self.char_index = 0
        self.char = tk.StringVar(root, "")
        self.pre_string = tk.StringVar(root, "")
        self.post_string = tk.StringVar(root, "")
        self.encodings = {
            "UTF-8": tk.StringVar(root, ""),
            "CP1252": tk.StringVar(root, ""),
        }
        self.utf8_link = None
        self._update()
        self.buttons = {}

    def _update(self):
        self.clipboard = self.raw_clipboard.decode(self.string_encoding)
        if self.char_index >= len(self.clipboard):
            self.char_index = len(self.clipboard) - 1
        self.char.set(self.clipboard[self.char_index])
        self.pre_string.set(self.clipboard[:self.char_index])
        self.post_string.set(self.clipboard[self.char_index + 1:])
        self.encodings['UTF-8'].set(encoding(self.char, "UTF-8"))
        self.encodings['CP1252'].set(encoding(self.char, "CP1252"))
        if self.utf8_link is not None:
            self.utf8_link.link = f"https://www.fileformat.info/info/unicode/char/{codepoint(self.char)}/index.htm"

    def left_press(self, event):
        self.char_index = max(self.char_index - 1, 0)
        self._update()
    
    def right_press(self, event):
        self.char_index = min(self.char_index + 1, len(self.clipboard) - 1)
        self._update()

    def change_clipboard_encoding(self, new_encoding):
        self.string_encoding = new_encoding
        for encoding, encoding_button in self.buttons.items():
            encoding_button.configure(background= "white" if encoding == new_encoding else "grey")
        self._update()

    def next_clipboard_encoding(self):
        encodings = list(self.buttons.keys())
        new_encoding = dict(zip(encodings, encodings[1:] + [encodings[0]]))[self.string_encoding]
        self.change_clipboard_encoding(new_encoding)


root = tk.Tk()
state = State()


def layout_root():
    root.geometry("400x150")
    root.title("Encoding Checker")
    root.grid_rowconfigure(0, weight=2)
    root.grid_rowconfigure(1, weight=10)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=5)
    root.grid_columnconfigure(1, weight=1)

    root.bind("<KeyPress-Left>", state.left_press)
    root.bind("<KeyPress-Right>", state.right_press)
    root.bind("<KeyPress-Up>", lambda _: state.next_clipboard_encoding())
    root.bind("<KeyPress-Down>", lambda _: state.next_clipboard_encoding())
    return root


def layout_characters(root):
    frame1 = tk.Frame(root)
    frame1.grid(row=0, column=1, sticky="nsew")

    frame2 = tk.Frame(frame1, highlightbackground="black", highlightthickness=1)
    frame2.grid(row=0, column=0, sticky="nsew")

    frame3 = tk.Frame(frame1, highlightbackground="black", highlightthickness=1)
    frame3.grid(row=0, column=1, sticky="nsew")

    state.utf8_link = link.Link(frame2, text="UTF-8")
    state.utf8_link.grid(row=1, column=1, sticky="EW")

    link.Link(frame3, link=f"https://www.i18nqa.com/debug/table-iso8859-1-vs-windows-1252.html", text="CP1252").grid(row=1, column=2, sticky="EW")
    tk.Label(frame2, textvariable=state.encodings["UTF-8"]).grid(row=0, column=1, sticky="EW")
    tk.Label(frame3, textvariable=state.encodings["CP1252"]).grid(row=0, column=2, sticky="EW")


def layout_message(root):
    frame = tk.Frame(root)
    frame.grid(row=1, column=0, sticky="nsew")
    root.grid_columnconfigure(0, weight=500)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=500)

    tk.Label(frame, textvariable=state.pre_string).grid(row=0, column=0, sticky="NES")    
    tk.Label(frame, textvariable=state.char, background="yellow").grid(row=0, column=1, sticky="NSEW")    
    tk.Label(frame, textvariable=state.post_string).grid(row=0, column=2, sticky="NWS")


def layout_buttons(root):
    frame = tk.Frame(root)
    frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    state.buttons['UTF-8'] = tk.Button(frame, text="Show As UTF-8", command=lambda: state.change_clipboard_encoding("UTF-8"))
    state.buttons['UTF-8'].pack(side=tk.LEFT, expand=True)
    state.buttons['CP1252'] = tk.Button(frame, text="Show As CP1252", command=lambda: state.change_clipboard_encoding("CP1252"), background="grey")
    state.buttons['CP1252'].pack(side=tk.LEFT, expand=True)


def main():
    root = layout_root()
    layout_characters(root)
    layout_message(root)
    layout_buttons(root)
    root.mainloop()


if __name__ == "__main__":
    main()