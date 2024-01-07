def hangman(word):
    wrong = 0
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
    rletters = list(word)
    return rletters

print(hangman('vova'))

