from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


if __name__ == '__main__':
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)

