import InputDialogs
import ConfigAutomaton
import State


def moveState(currState):
    inp = InputDialogs.getInput()
    for trans in transList:
        if trans['word'] == inp and trans['fromState'] == currState:
            currState = trans['toState']
            if currState == '3':
                print('Τερματική Κατασταση')
                exit('Exiting')
            else:
                print('Μη Τερματική Κατάσταση')
                moveState(currState)


if __name__ == '__main__':
    descriptionFile = InputDialogs.loadDescriptionFile()
    print(f'description file added: {descriptionFile}')
    automatic = ConfigAutomaton.returnAutomaton(descriptionFile)
    print(f'automatic is: \n{automatic}')
    transList = State.separateTransition(automatic[5:])  # pass only transitions
    print(transList)
    moveState(str(automatic[1]))

