import pyperclip
import os
import tkinter as tk

# entries stores the clipboard contents
entries = []


# Updates the clipboard with new copied text
def update_board():
    entry = pyperclip.paste()
    if entry is not None and entry not in entries:
        entries.append(entry)
        label.config(text=entry)
        # board is the file object storing the clipboard
        board = open("clip.txt", "a+")  # by default, the entries are stored in a file called "clip.txt"
        board.write('\n' + entry)
        board.close()
    root.after(10, update_board)


# Main Program
if __name__ == '__main__':
    root = tk.Tk()
    os.chdir('/Users/dillonyu/Desktop/')  # will change to universal Desktop location later
    label = tk.Label(root, text="Things you copy show up here")
    label.pack()
    update_board()
    root.mainloop()
