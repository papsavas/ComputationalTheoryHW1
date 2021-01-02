from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
from State import emtpyWord


def loadDescriptionFile():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def receiveUserInput():
    Tk().withdraw()
    while simpledialog.ACTIVE == 'active':
        return simpledialog.askstring(title="Input Dialog",
                                      prompt="Insert a character:\n Empty Word = " + emtpyWord)


def showError(errorMessage):
    showerror(title="Error", message=errorMessage)
