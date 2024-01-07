def hangman(word):
    # initialise count for wrong count of user
    wrong = 0
    # caribbean hangman shape
    stages = [
        '_____________', 
        '|            ',
        '|     ___    ',
        '|    //|\\   ',
        '|  --------- ',
        '|    (   )   ',
        '|      |     ',
        '|   __| |__  ',
        '|     | |    ', 
        '|    _| |_    '
    ]
    # create a list of the called on word for hangman game
    rletters = list(word)
    # underside of the letter, multiplied by the amount of letters in the chosen word
    board = ['__'] * len(word)
    win = False
    print('Welcome to Caribbean Hangman!')

