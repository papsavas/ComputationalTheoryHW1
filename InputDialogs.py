from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog

from numpy.core.defchararray import strip


def loadDescriptionFile():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def receiveUserInput():
    Tk().withdraw()
    return strip(str(simpledialog.askstring(title="Input Dialog",
                                            prompt="Insert a character:\n Empty Word = ")))


def getInput():
    while True:
        userInput = receiveUserInput()
        print('user input: ' + str(userInput))
        if userInput == 'None' or userInput is None:
            return None
        if not userInput == '':
            break
        showError('You need to add a character or a word. To exit, press "X" or "Cancel"')
    return userInput


def showError(errorMessage):
    showerror(title="Error", message=errorMessage)
