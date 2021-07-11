import pyperclip
import os
import tkinter as tk

# entries stores the clipboard contents as strings
entries = []
# buttons stores the clipboard contents as button objects
buttons = []
# nextButton stores the index of the next button to store the latest entry
nextButton = 0
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


# Updates the clipboard with new copied text
def update_board():
    global nextButton
    entry = pyperclip.paste()
    if entry is not None and not entry.isspace() and entry not in entries:
        entries.append(entry)
        if nextButton >= len(buttons):
            nextButton = 0
        buttons[nextButton].config(text=entry)
        nextButton += 1
    root.after(10, update_board)


def copy_text(text):
    if text.isspace():
        return
    pyperclip.copy(text)


# Main Program
if __name__ == '__main__':
    for i in range(10):
        button = tk.Button(frame,
                           text="",
                           anchor='nw',
                           justify='left',
                           height=3,
                           width=100,
                           wraplength=899)
        # command=lambda: copy_text('Hi!'))
        button.config(command=lambda b=button: copy_text(b['text']))
        button.pack()
        buttons.append(button)
    update_board()
    root.mainloop()
