import pyperclip

# entries stores the clipboard contents
entries = []


# Updates the clipboard with new copied text
def update_board():
    entry = pyperclip.paste()
    if entry not in entries:
        entries.append(entry)
        print(entries)


while True:
    update_board()
