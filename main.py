import tkinter as tk
import link



def codepoint(byt):
    try:
        byt = byt.decode("UTF-8")[0]
    except UnicodeDecodeError:
        return "-1"
    return hex(ord(byt))[2:]


def encoding(byt, encoding):
    try:
        return byt.decode(encoding)
    except:
        return "Decode Error"

copied_text = "My name is Matthew"
root = tk.Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=5)
root.grid_rowconfigure(1, weight=5)
root.grid_columnconfigure(1, weight=1)

frame1 = tk.Frame(root)
frame1.grid(row=0, column=1, sticky="nsew")

frame2 = tk.Frame(frame1, highlightbackground="black", highlightthickness=1)
frame2.grid(row=0, column=0, sticky="nsew")

frame3 = tk.Frame(frame1, highlightbackground="black", highlightthickness=1)
frame3.grid(row=0, column=1, sticky="nsew")


x = b"\xD6"
link.Link(frame2, link=f"https://www.fileformat.info/info/unicode/char/{codepoint(x)}/index.htm", text="UTF-8").grid(row=1, column=1, sticky="EW")
link.Link(frame3, link=f"https://www.i18nqa.com/debug/table-iso8859-1-vs-windows-1252.html", text="CP1252").grid(row=1, column=2, sticky="EW")
tk.Label(frame2, text=encoding(x, "UTF-8")).grid(row=0, column=1, sticky="EW")
tk.Label(frame3, text=encoding(x, "CP1252")).grid(row=0, column=2, sticky="EW")
tk.Label(text=copied_text).grid(row=1, column=0)

root.mainloop()