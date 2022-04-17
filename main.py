import tkinter as tk
import link


class State:
    def __init__(self) -> None:
        self.char_index = 5
        self.clipboard = root.clipboard_get()
        self.char = tk.StringVar(root, "")
        self.pre_string = tk.StringVar(root, "")
        self.post_string = tk.StringVar(root, "")
        self._update()
    
    def _update(self):
        self.char.set(self.clipboard[self.char_index])
        self.pre_string.set(self.clipboard[:self.char_index])
        self.post_string.set(self.clipboard[self.char_index + 1:])

    def left_press(self, event):
        self.char_index = max(self.char_index - 1, 0)
        self._update()
    
    def right_press(self, event):
        self.char_index = min(self.char_index + 1, len(self.clipboard) - 1)
        self._update()


root = tk.Tk()
state = State()


def layout_root():
    root.geometry("400x150")
    root.grid_rowconfigure(0, weight=2)
    root.grid_rowconfigure(1, weight=10)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=5)
    root.grid_columnconfigure(1, weight=1)

    root.bind("<KeyPress-Left>", state.left_press)
    root.bind("<KeyPress-Right>", state.right_press)
    return root


def layout_characters(root):
    def codepoint(byt):
        return hex(ord(byt.get()[0]))[2:]


    def encoding(byt, encoding):
        print(byt.get())
        try:
            return byt.get().decode(encoding)
        except:
            return "Decode Error"

    frame1 = tk.Frame(root)
    frame1.grid(row=0, column=1, sticky="nsew")

    frame2 = tk.Frame(frame1, highlightbackground="black", highlightthickness=1)
    frame2.grid(row=0, column=0, sticky="nsew")

    frame3 = tk.Frame(frame1, highlightbackground="black", highlightthickness=1)
    frame3.grid(row=0, column=1, sticky="nsew")

    link.Link(frame2, link=f"https://www.fileformat.info/info/unicode/char/{codepoint(state.char)}/index.htm", text="UTF-8").grid(row=1, column=1, sticky="EW")
    link.Link(frame3, link=f"https://www.i18nqa.com/debug/table-iso8859-1-vs-windows-1252.html", text="CP1252").grid(row=1, column=2, sticky="EW")
    tk.Label(frame2, textvariable=encoding(state.char, "UTF-8")).grid(row=0, column=1, sticky="EW")
    tk.Label(frame3, textvariable=encoding(state.char, "CP1252")).grid(row=0, column=2, sticky="EW")


def layout_message(root):
    frame = tk.Frame(root)
    frame.grid(row=1, column=0, sticky="nsew")
    tk.Label(frame, textvariable=state.pre_string).pack(side=tk.LEFT)    
    tk.Label(frame, textvariable=state.char, background="yellow").pack(side=tk.LEFT)    
    tk.Label(frame, textvariable=state.post_string).pack(side=tk.LEFT)    


def layout_buttons(root):
    frame = tk.Frame(root)
    frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    tk.Button(frame, text="Show As UTF-8").pack(side=tk.LEFT, expand=True)
    tk.Button(frame, text="Show As CP1252").pack(side=tk.LEFT, expand=True)


def main():
    root = layout_root()
    layout_characters(root)
    layout_message(root)
    layout_buttons(root)
    root.mainloop()


if __name__ == "__main__":
    main()