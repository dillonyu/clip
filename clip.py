import pyperclip
import tkinter as tk

# entries stores the clipboard contents as strings
entries = []
# entry_buttons stores the clipboard contents as button objects
entry_buttons = []
# delButtons stores the delete buttons 
del_buttons = []
# next_button stores the index of the next button to store the latest entry
next_button = 0
root = tk.Tk()
root.geometry("660x525")
frame = tk.Frame(root)


# Updates the clipboard with new copied text
def update_board():
    global next_button
    entry = pyperclip.paste()
    if entry is not None and not entry.isspace() and entry != '' and entry not in entries:
        entries.append(entry)
        if next_button >= len(entry_buttons):
            shift_text_up(1)
            next_button -= 1
        entry_buttons[next_button].config(text=entry)
        next_button += 1
    root.after(10, update_board)


# Copies the input text
def copy_text(text):
    if text.isspace():
        return
    pyperclip.copy(text)


# Shifts all clipboard contents up when not enough space is available for a new entry
def shift_text_up(i):
    if i == len(entry_buttons):
        entry_buttons[i - 1].config(text='')
    for a in range(i, len(entry_buttons)):
        next_text = entry_buttons[a].cget('text')
        entry_buttons[a - 1].config(text=next_text)
        if a == len(entry_buttons) - 1:
            entry_buttons[a].config(text='')


# Opens a new window to display the full text on a clipboard entry
def expand_text():
    pass

# Deletes an entry based on the input index
def del_entry(i):
    global next_button
    if entry_buttons[i].cget('text').isspace() or entry_buttons[i].cget('text') == '':
        print('Empty!')
        return
    del entries[i]
    print(entries)
    shift_text_up(i+1)
    next_button -= 1


# Main Program
for i in range(10):
    button = tk.Button(text="",
                       anchor='nw',
                       justify='left',
                       height=3,
                       width=57,
                       wraplength=500)
    button.config(command=lambda b=button: copy_text(b['text']))
    button.grid(row=i, column=0)
    entry_buttons.append(button)

    expand_button = tk.Button(justify='right', 
                              height=3, 
                              width=10, 
                              text="Expand", 
                              fg="blue")
    expand_button.grid(row=i, column=1)

    del_button = tk.Button(justify='right', 
                           height=3, 
                           width=5, 
                           text="X", 
                           fg="red")
    del_button.grid(row=i, column=2)
    del_buttons.append(del_button)
    del_button.config(command=lambda d=del_button: del_entry(del_buttons.index(d)))

print(entries)
update_board()
root.mainloop()
