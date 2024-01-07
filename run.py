import random
def opening():
    category_message = 'Please choose a category to begin the game:'
    print('\nFor "Easy", press "e"')
    print('\nFor "Medium", press "m"')
    print('\nFor "Hard", press "h"')
    chosen = input(category_message)
    return chosen

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
        else:
            # Increment wrong score.
            wrong += 1
        # Print the full board for reference.
        print((' '.join(board)))
        
        e = wrong + 1
        # Print the relative number of hangman stages based on number of wrong inputs.
        print('\n'.join(stages[0:e]))

        # Check for win condition.
        if '__' not in board:
            print('\nYou win! \nCaribbean man is free.')
            print(''.join(board))
            win = True
            break

    # Print losing statements and let user know what the correct answer was.
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('\nRIP Caribbean man! \nBetter luck next time.')
        print(f'The answer was "{word}".')

def main():
    pass
main()