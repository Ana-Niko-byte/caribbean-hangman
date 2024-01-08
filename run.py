import random
import pyfiglet 
def opening():
    # Convert text to ASCII art
    ascii_art = pyfiglet.figlet_format("Caribbean Hangman")
    # Print the ASCII art
    print(ascii_art + '\n')
    category_message = 'Please choose a category to begin the game: '
    print('\nFor "Easy", press "e"')
    print('\nFor "Medium", press "m"')
    print('\nFor "Hard", press "h"')
    chosen = input(category_message)
    return chosen

def category_selection():
    """
    This function handles category selection and uses words from the relative list.
    """
    # The value the user chose for the game category.
    category = opening().lower()
    if category == 'e':
        print('\nYou have chosen Easy! Have fun!')
        easy_category = [
            "apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jar",
            "kite", "lion", "mouse", "nest", "orange", "pig", "queen", "rat", "snake", 
            "tree", "umbrella", "van", "wolf", "xray", "yarn", "zebra"
        ]
        # Randomly selects a word from the list.
        chosen_word = random.choice(easy_category)
        return chosen_word
    elif category == 'm':
        print('\nYou have chosen Medium! Enjoy!')
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
    else:
        print(f'Invalid entry for category selection.\nYou typed {category}.')
        raise f'Invalid entry for category selection.\nYou typed "{category}".'
    
def stages():
    """
    This function stores the 'stages' of the hangman game.
    """
    # Caribbean hangman shape.
    # Note: the '\\\\' part of the hat is '\\' being escaped by '\\' due to the way python deals with strings.
    stages = [
        '_____________    ', 
        '|          |     ',
        '|          |     ',
        '|         ___    ',
        '|        //|\\\\ ',
        '|      --------- ',
        '|       ( ._. )  ',
        '|          |     ',
        '|       __| |__  ',
        '|         |_|    ',
        '|         | |    ', 
        '|        _| |_   ',
        '|                ',
        '|                ',
        '|_____________   ',
    ]
    return stages

def hangman(word):
    """
    This is the main function for the hangman game. 
    It handles conditions for user input,
    """
    # Initialise count for wrong count of user.
    wrong = 0
    hangman_stages = stages()
    # Create a list of the called on word for hangman game.
    rletters = list(word)
    # Underside of the letter, multiplied by the amount of letters in the chosen word.
    # Two underscores per letter.
    board = ['__'] * len(word)
    win = False
    print('Welcome to Caribbean Hangman!')

    while wrong < len(hangman_stages):
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

        e = wrong + 1
        # Print the relative number of hangman stages based on number of wrong inputs.
        print('\n'.join(hangman_stages[0:e]))
        # Print the full board for reference.
        print((' '.join(board)))

        # Check for win condition.
        if '__' not in board:
            print('\nYou win! \nCaribbean man is free.')
            print(''.join(board))
            win = True
            break

    # Print losing statements and let user know what the correct answer was.
    if not win:
        print('\n'.join(hangman_stages[0:wrong]))
        print('\nRIP Caribbean man! \nBetter luck next time.')
        print(f'The answer was "{word}".')

def main():
    """
    This function calls all functions for the game to work.
    """
    category_word = category_selection()
    hangman(category_word)
main()