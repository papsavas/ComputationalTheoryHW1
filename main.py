import InputDialogs

if __name__ == '__main__':
    descriptionFile = InputDialogs.loadDescriptionFile()
    print(f'description file added: {descriptionFile}')
    inp = InputDialogs.receiveUserInput()
    print(inp)
    while inp is not None:
        if inp is '':
            InputDialogs.showError('You need to add a character. '
                                   'If you want to exit, close the window or press "Cancel"')
        inp = InputDialogs.receiveUserInput()
        print(inp)
