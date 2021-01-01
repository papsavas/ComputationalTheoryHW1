emtpyWord = "#"


def separateTransition(transitions):
    transitionList = []
    for tr in transitions:
        args = tr.split(' ')
        transitionList.append({
            "from": args[0],
            "with": args[1],
            "to": args[2]
        })
    print(transitionList)

