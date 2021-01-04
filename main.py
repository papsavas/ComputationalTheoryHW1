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
        if not moveState(char):
            return askInput()
    return askInput()


def moveState(c):
    # returns bool dictating if a transition occurred
    global automaton
    if c not in automaton.alphabet:
        UserDialogs.showErrorDialog(f'Character {c} is not contained in automatons alphabet: {automaton.alphabet}')
        askInput()
    if c == automaton.emptyWord:
        print('Empty Word Transition. Current States: ' + str(automaton.currentStates))
        return True
    moved = False
    sessionStates = []
    for trans in automaton.transitions:
        if trans['word'] == c and trans['fromState'] in automaton.currentStates:
            sessionStates.append(trans['toState'])
            if sessionStates[-1] in automaton.terminalStates:
                print(f'Terminal State reached. Transition: [{trans["fromState"]} -({trans["word"]})-> {trans["toState"]}]')
                print('Terminal State: ' + trans['toState'])
                moved = True
            else:
                print(f'Transition: [{trans["fromState"]} -({trans["word"]})-> {trans["toState"]}]')
                print('Non Terminal State: ' + trans['toState'])
                moved = True
    automaton.currentStates.clear()
    automaton.currentStates = sessionStates
    return moved


if __name__ == '__main__':
    descriptionFile = UserDialogs.loadDescriptionFile()
    print(f'description file added: {descriptionFile}')
    automaton = ConfigAutomaton.Automaton(descriptionFile)
    print('automaton transitions:\n' + str(automaton.transitions))
    askInput()
