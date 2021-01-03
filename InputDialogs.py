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
    return str(simpledialog.askstring(title="Input Dialog",
                                      prompt="Insert a character:\n Empty Word = " + emtpyWord))


def getInput():
    while True:
        userInput = receiveUserInput()
        print('user input: '+userInput)
        if userInput is not None and userInput is not '':
            break
    return userInput


def showError(errorMessage):
    showerror(title="Error", message=errorMessage)
