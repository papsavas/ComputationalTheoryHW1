"""
Author:
Papageorgiadis Savvas
dai18001
@papsavas
"""

import UserDialogs
import ConfigAutomaton


def askInput():
    global automaton
    inp = UserDialogs.getInput()
    if inp is None:
        print('User Exited')
        exit(0)
    inp = str(inp)  # since its not 'None', its needed as string and not as ndarray
    for char in inp:
        if moveState(char) == 1:
            return askInput()
    return askInput()


def moveState(c):
    # return codes:
    # 0 -> moved
    # 1 -> did not found transition
    global automaton
    if c not in automaton.alphabet:
        UserDialogs.showErrorDialog(f'Character {c} is not contained in automatons alphabet: {automaton.alphabet}')
        askInput()

    for trans in automaton.transitions:
        if trans['word'] == c and trans['fromState'] == automaton.currentState:
            automaton.currentState = trans['toState']
            if automaton.currentState in automaton.terminalStates:
                print('Terminal State: ' + automaton.currentState)
                print('Terminal State reached. Transitioned with: ' + str(trans))
                return 0
            else:
                print('Non Terminal State: ' + automaton.currentState)
                print('Transitioned with ' + str(trans))
                return 0
    return 1


if __name__ == '__main__':
    descriptionFile = UserDialogs.loadDescriptionFile()
    print(f'description file added: {descriptionFile}')
    automaton = ConfigAutomaton.Automaton(descriptionFile)
    print('automaton transitions:\n' + str(automaton.transitions))
    askInput()
