emtpyWord = "#"


def separateTransition(transitions):
    transitionList = []
    for tr in transitions:
        args = tr.split(' ')
        transitionList.append({
            "fromState": args[0],
            "word": args[1],
            "toState": args[2]
        })
    return transitionList


