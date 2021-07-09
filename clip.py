from multiprocessing import Process

import pyperclip
import os

# entries stores the clipboard contents
entries = []


# Updates the clipboard with new copied text
def update_board():
    entry = pyperclip.paste()
    if entry != None and entry not in entries:
        entries.append(entry)
        # board is the file object storing the clipboard
        board = open("clip.txt", "a+") # by default, the entries are stored in a file called "clip.txt"
        board.write('\n' + entry)
        # board.seek(0)
        # print(board.read())
        board.close()

        # print(entries)

# def runInParallel(*fns):
#   proc = []
#   for fn in fns:
#     p = Process(target=fn)
#     p.start()
#     proc.append(p)
#   for p in proc:
#     p.join()

# def test():
#         while True:
#             print('View Clipboard (view)')
#             response = str(input())
#             if response == 'view':
#                 break
#         print('Viewing Clipboard...')

# Main Program
# if __name__ == '__main__':
#     p1 = Process(target=update_board)
#     p1.start()
#     p2 = Process(target=test)
#     p2.start()
#     p1.join()
#     p2.join()
#     os.chdir('/Users/dillonyu/Desktop/') # will change to universal Desktop location later
#     print('Welcome to Clip! What would you like to do?')
#     # while True:
#         # update_board()
#     while True:
#         runInParallel(update_board, test)

print('Welcome to Clip! What would you like to do?')
while True:
    update_board()
