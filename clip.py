import pyperclip
import os

# entries stores the clipboard contents
entries = []


# Updates the clipboard with new copied text
def update_board():
    entry = pyperclip.paste()
    if entry not in entries:
        entries.append(entry)
        # board is the file object storing the clipboard
        board = open("clip.txt", "a") # by default, the entries are stored in a file called "clip.txt"
        board.write(entry)
        board.close()

        # print(entries)

print(os.getcwd()) # for testing only
while True:
    update_board()
