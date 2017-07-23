from tkinter import *
import sys
def quit():
    print('Hello, I\'m going')
    sys.exit()

root = Tk()
widget = Label(root)
widget = Button(None, text = 'Hello GUI Word!', command = quit)
widget.pack(side = TOP, expand = YES, fill = BOTH)
root.title('Gui01.py')
root.mainloop()