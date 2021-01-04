from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
from numpy.core.defchararray import strip


def loadDescriptionFile():
    Tk().withdraw()
    filename = askopenfilename(title="Select Automaton Configuration Document", filetypes=(('text files', 'txt'),))
    return filename


def receiveUserInput():
    Tk().withdraw()
    return strip(str(simpledialog.askstring(title="Input Dialog",
                                            prompt="Insert a character:\n Empty character = #")))


def getInput():
    while True:
        userInput = receiveUserInput()
        print('user input: ' + str(userInput))
        if userInput == 'None' or userInput is None:
            return None
        if not userInput == '':
            break
        showErrorDialog('You need to add a character or a word. To exit, press "X" or "Cancel"')
    return userInput


def showErrorDialog(errorMessage):
    showerror(title="Error", message=errorMessage)
