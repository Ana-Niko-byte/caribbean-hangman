import random
def opening():
    category_message = 'Please choose a category to begin the game:'
    print('\nFor "Easy", press "e"')
    print('\nFor "Medium", press "m"')
    print('\nFor "Hard", press "h"')
    chosen = input(category_message)
    return chosen

def category_selection():
    """
    This function handles category selection and uses words from the relative list.
    """
    category = opening()
    try:
        if category == 'e':
            print('\nYou have chosen Easy!')
            easy_category = [
                "apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jar",
                "kite", "lion", "mouse", "nest", "orange", "pig", "queen", "rat", "snake", 
                "tree", "umbrella", "van", "wolf", "xray", "yarn", "zebra"
            ]
            chosen_word = random.choice(easy_category)
            return chosen_word
        elif category == 'm':
            print('\nYou have chosen Medium!')
            medium_category = [
                "banana", "cactus", "dragon", "elephant", "flamingo", "giraffe", "hamburger",
                "internet", "jungle", "kangaroo", "library", "mountain", "notebook", 
                "octopus", "penguin", "quartz", "rainbow", "squirrel", "triangle", 
                "umbrella", "volcano", "waffle", "xylophone", "yogurt", "zeppelin"
            ]
            chosen_word = random.choice(medium_category)
            return chosen_word
        elif category == 'h':
            print('\nYou have chosen Hard! Good luck!')
            hard_category = [
                "abstract", "buzzard", "cryptic", "dwarves", "espionage", "fjord", 
                "gazebo", "hyphen", "ivory", "jigsaw", "kayak", "labyrinth", 
                "mystique", "numbskull", "oxygen", "pixel", "quarantine", "rhythm", 
                "sphinx", "tundra", "unzip", "vortex", "waltz", "xylophone", 
                "yacht", "zodiac"
            ]
            chosen_word = random.choice(hard_category)
            return chosen_word
    except ValueError as e:
        raise f'Invalid entry for category selection.\nYou typed {e}'

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