def hangman(word):
    # Initialise count for wrong count of user.
    wrong = 0
    # Caribbean hangman shape.
    stages = [
        '_____________', 
        '|            ',
        '|     ___    ',
        '|    //|\\   ',
        '|  --------- ',
        '|   ( ._. )  ',
        '|      |     ',
        '|   __| |__  ',
        '|     | |    ', 
        '|    _| |_    '
    ]
    # Create a list of the called on word for hangman game.
    rletters = list(word)
    # Underside of the letter, multiplied by the amount of letters in the chosen word.
    # Two underscores per letter.
    board = ['__'] * len(word)
    win = False
    print('Welcome to Caribbean Hangman!')

    while wrong < len(stages):
        # On new line, ask for letter input.
        print('\n')
        message = 'Guess a letter:'
        letter = input(message)

        # Set condition to check if inputted letter is in the list of letters.
        if letter in rletters:
            # Find the index of the guessed letter in the list.
            letter_index = rletters.index(letter)
            # Set the guessed letter to the same index in the board list.
            board[letter_index] = letter
            # Replace the guessed letter with a different symbol so that it is not pisked up again. 
            rletters[letter_index] = '*'
hangman('wait')
