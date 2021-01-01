import InputDialogs
import ConfigAutomaton
import State
if __name__ == '__main__':
    descriptionFile = InputDialogs.loadDescriptionFile()
    print(f'description file added: {descriptionFile}')
    automatic = ConfigAutomaton.returnAutomaton(descriptionFile)
    print(f'automatic is: \n{automatic}')
    State.separateTransition(automatic[5:])
    exit(2)
    inp = InputDialogs.receiveUserInput()
    print(inp)
    while inp is not None:
        if inp is '':
            InputDialogs.showError('You need to add a character. '
                                   'If you want to exit, close the window or press "Cancel"')
        inp = InputDialogs.receiveUserInput()
        print(inp)
