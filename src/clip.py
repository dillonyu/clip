import pyperclip
import tkinter as tk
from tkinter import messagebox as mb
import webbrowser

# entries stores the clipboard contents as strings
entries = []
# entry_buttons stores the clipboard contents as button objects
entry_buttons = []
# del_buttons stores the delete buttons
del_buttons = []
# expand_buttons stores the expand buttons
expand_buttons = []
# next_space stores the index of the next available space to store the newest entry
next_space = 0
# full is True when all 10 spots in the clipboard are filled, and False otherwise
full = False

root = tk.Tk()
root.geometry("616x557")
root.title('Clip')


# Updates the clipboard with any new copied text
def update_board():
    entry = pyperclip.paste()
    if type(entry) is not None and entry != '' and not entry.isspace() and entry not in entries:
        entries.append(entry)
        add_entry(entry)
    root.after(100, update_board)


# Shifts all clipboard content up from index top, deleting the entry at index top - 1
def shift_entries_up(top):
    if full:
        del entries[0]
    for a in range(top, len(entry_buttons)):
        next_text = entry_buttons[a].cget('text')
        entry_buttons[a - 1].config(text=next_text)
    entry_buttons[len(entry_buttons) - 1].config(text='')


# Opens a new window to display the full text on a clipboard entry
def expand_entry(expand_index):
    ans = mb.askokcancel('Full Text', 'Full Text:\n\n \" ' + entries[expand_index] + " \"" + '\n\nCopy Text?')
    if ans:
        pyperclip.copy(entries[expand_index])


# Adds the input text as an entry to the clipboard
def add_entry(new_text):
    global next_space
    global full
    if entries:
        clr_all_button.config(state='normal')
    # adjusts accordingly if the clipboard is full
    if next_space >= len(entry_buttons):
        full = True
        shift_entries_up(1)
        next_space -= 1
    # truncates long text
    if len(new_text) > 200:
        entry_buttons[next_space].config(text=new_text[:200] + '...', state='normal')
    else:
        entry_buttons[next_space].config(text=new_text, state='normal')
    del_buttons[next_space].config(text='X', fg='red', state='normal')
    expand_buttons[next_space].config(text='...', fg='blue', state='normal')
    next_space += 1


# Deletes an entry based on the input index
def del_entry(del_index):
    global next_space
    global full
    del entries[del_index]
    pyperclip.copy('')
    full = False
    shift_entries_up(del_index + 1)
    next_space -= 1
    entry_buttons[next_space].config(state='disabled')
    del_buttons[next_space].config(text='', state='disabled')
    expand_buttons[next_space].config(text='', state='disabled')
    if not entries:
        clr_all_button.config(state='disabled')


# Clears all entries from the clipboard
def clear_all():
    global next_space
    ans = mb.askquestion('Clear Clipboard', 'Are you sure you want to clear the clipboard?')
    if ans == 'yes':
        for b in range(len(entry_buttons)):
            entry_buttons[b].config(text='', state='disabled')
            expand_buttons[b].config(text='', state='disabled')
            del_buttons[b].config(text='', state='disabled')
        next_space = 0
        entries.clear()
        pyperclip.copy('')
        clr_all_button.config(state='disabled')


# Opens a link to help on using the program
def open_help():
    webbrowser.open('https://github.com/dillonyu/clip#usage')


# Main Program
for i in range(10):
    button = tk.Button(text="",
                       anchor='n',
                       height=3,
                       width=57,
                       wraplength=500,
                       state='disabled')
    button.config(command=lambda b=button: pyperclip.copy(entries[entry_buttons.index(b)]))
    button.grid(row=i, column=0)
    entry_buttons.append(button)

    expand_button = tk.Button(height=3,
                              width=5,
                              state='disabled')
    expand_button.config(command=lambda b=expand_button: expand_entry(expand_buttons.index(b)))
    expand_buttons.append(expand_button)
    expand_button.grid(row=i, column=1)

    del_button = tk.Button(height=3,
                           width=5,
                           state='disabled')
    del_button.grid(row=i, column=2)
    del_buttons.append(del_button)
    del_button.config(command=lambda d=del_button: del_entry(del_buttons.index(d)))

clr_all_button = tk.Button(text="Clear All",
                           height=2,
                           width=57,
                           fg='red',
                           state='disabled')
clr_all_button.grid(row=10, column=0)
clr_all_button.config(command=clear_all)

help_button = tk.Button(text="Help",
                        height=2,
                        width=10,
                        command=open_help)
help_button.grid(row=10, column=1, columnspan=2, sticky=tk.W + tk.E)

pyperclip.copy('')
update_board()
root.mainloop()
