from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog


def loadDescriptionFile():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def receiveUserInput():
    Tk().withdraw()
    while simpledialog.ACTIVE == 'active':
        return simpledialog.askstring(title="Εισαγωγή Χαρακτήρα",
                                      prompt="Insert a character:")


def showError(errorMessage):
    showerror(title="Error", message=errorMessage)
