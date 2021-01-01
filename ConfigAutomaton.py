import pandas as pd


# numpy 1.94.4 may cause an error on Windows OS.
# If an error presents, install numpy 1.19.3 instead
# 'pip install numpy==1.19.3'


def returnAutomaton(configPath):
    with open(configPath) as file:
        data = file.read().splitlines()
    return data
