import pandas as pd


# numpy 1.94.4 may cause an error on Windows OS.
# If an error presents, install numpy 1.19.3 instead
# 'pip install numpy==1.19.3'


def returnAutomatic(configPath):
    data = pd.read_csv(configPath, sep="\n", header=None)
    transitionText = (len(data) - 5) * ['transition']
    data.index = ["n.o_states", "starting_state", "n.o_ending_states", "ending_states",
                  "n.o_transitions", *transitionText]
    return data
