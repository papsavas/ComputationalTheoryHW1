
class Automaton:
    def __init__(self, configFilePath):
        with open(configFilePath) as file:
            data = file.read().splitlines()
            self.emptyWord = "#"
            self.numOfStates = int(data[0])
            self.startingState = str(data[1])
            self.currentState = self.startingState
            self.terminalStates = list(str(data[3]))
            assert data[2].isdigit(), 'Terminal States number (line 3) must be a positive Integer'
            self.terminalStatesNum = int(data[2])
            assert data[4].isdigit(), 'The number of transitions (line 5) must be a positive Integer'
            self.transitionsNum = int(data[4])
            self.transitions = []
            self.alphabet = set()
            self.alphabet.add(self.emptyWord)
            for tr in data[5:]:
                args = tr.split(' ')
                self.alphabet.add(args[1])
                self.transitions.append({
                    "fromState": args[0],
                    "word": args[1],
                    "toState": args[2]
                })
            assert len(self.transitions) == self.transitionsNum, f'Declared {self.transitionsNum} transitions but ' \
                                                                 f'provided {len(self.transitions)} '
