# Import the random module to generate a random word
import random
# Alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of potential yes words the player can choose from
yes = ['y', 'yes', 'ya', 'yep', 'yup', 'yeh', 'ye', 'yea', 'totally', 'sure', 'ok', 'okay', 'alright', 'alrighty', 'alrighty then', 'certainly', 'definitely', 'glady', 'absolutely', 'indeed', 'undoubtedly', 'fine', 'aye', 'surely', 'mmhmm', 'mhmm', 'of course', 'k', 'kk', 'very well', 'for sure', 'you bet', 'no problem', 'i guess so', 'why not', 'hell yes','hell yea', 'heck yea', 'naturally', 'okie dokie', 'affirmative', 'aye aye', 'uh huh', 'yuppers', 'yes sir', 'yes mam', 'by all means', 'cool', 'no problem', 'sure why not', 'sure no problem', 'i do', 'love to', 'good', 'as you wish', 'i shall', 'sure i can', 'willingly', 'exactly', 'for sure', 'si', 'hao', 'da', 'ja', 'hai', 'sim', 'oui', 'ayo', 'yea sure']

# Define a list of words to use in the game
words = [
    'elephant','umbrella','sprint','keyboard','volcano','hopscotch','waterfall','jellyfish','frozen', 'giraffe', 'flamingo','peacock','chirping','shipwreck','stretching','crawling','seagull','dolphin','hummingbird',
    'leaping','dancing','whistling','singing','clapping','laughing','giggling','smiling','grinning','candy',
    'icecream','waterfall','cookie','pancake','natural','avalanche','sandwich','woodchip','popcorn','mountain',
    'volcano','kingdom','milkshake','pinstripe','teapot','coffee', 'watermelon', 'blueberry', 'honeydew', ]
a_z = alphabet
# Define the individual parts of the hangman image
background = '☀🏰🚩☁         ☁'
rope = '     𓍯'
head = '     🤐'
dead = '     😵'
left_hand = '  O'
arm = '='
chest = '\_/'
right_hand = 'O'
left_leg = '     | '
right_left = '|'
left_foot = '     l '
right_foot = 'l'
hanged_body = [head, left_hand, arm, arm, chest, arm, arm, right_hand, left_leg, right_left, left_foot, right_foot]
full_body = '''
☀🏰🚩☁         ☁
        𓍯
       😵
    O==\_/==O
       | |
       l l  '''

# Generate a random word from the list
word = random.choice(words)

# Initialize an empty list to store the letters that have been guessed
guessed_letters = []

# Initialize a counter to keep track of the number of incorrect guesses
incorrect_guesses = 0

# Ask the player if they want to hear the instructions for the game
hangman_instructions = input(f'Would you like to hear instructions for the Hangman game?')
if hangman_instructions.strip().lower() in yes:
    input("\nHere is a set of instructions for the player to play the hangman game:\n\n1. A word will be randomly chosen from a list of words.\n\n2. The letters in the word will be hidden, and you will have to guess the letters in the word one by one.\n\n3. If a letter you guess is in the word, it will be revealed in the correct position in the word.\n\n4. If a letter you guess is not in the word, you will lose one chance. You have a total of 12 chances.\n\n5. You can also choose to guess the full word at any point during the game. If your guess is correct, you will win the game. If your guess is incorrect, you will lose one of your remaining chances.\n\n6. You win the game if you guess all the letters in the word before running out of chances, or if you correctly guess the full word.\n\n7. You lose the game if you run out of chances without guessing all the letters in the word.\nPress enter to continue...\n")
else:
    pass

# Print the remaining chances
remaining_chances = len(hanged_body)
print(f'Remaining Chances: {remaining_chances}')

# Start a loop to allow the player to guess letters
while incorrect_guesses < remaining_chances:
    # Prints the remaining and guessed letters. The code below also cleans up the strings to look more presentable.
    new_a_z = ', '.join(
    [f'{letter}' for letter in a_z])
    new_guessed_letter = ', '.join(
    [f'{letter}' for letter in guessed_letters])
    print(f'\nRemaining Letters: {new_a_z}')
    print(f'Guessed Letters: {new_guessed_letter}')
    # Print the hangman image, up to the number of incorrect guesses made
    print(f'\n{background}\n{rope}\n{head}')

    # Prompt the player to guess a letter
    guess = input('\nGuess the LETTER or WORD: ').lower()

    # If the letter input is a number like "5" or symbol like "^" then this message will be printed
    while guess not in alphabet:
        if guess != word:
            print('You must enter a letter in the alphabet. Please try again.')
        break

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter. Try again.')
    else:
        # Add the letter to the list of guessed letters
        if len(guess) == 1:
            if guess in alphabet:
                guessed_letters.append(guess)
                a_z.remove(guess)
                # Check if the player has won by guessing all the letters in the word
                if all(letter in guessed_letters for letter in word):
                    print('\nCongratulations, you won the game!')
                    break
                # If the letter is not in the word, increment the incorrect guess counter
                if guess not in word:
                    incorrect_guesses += 1
                    print('Sorry, please try again.')
            else:
                pass
        # Check if the letter is in the word
        elif guess in word:
            # Checks if the guess is more than one letter
            if len(guess) > 1:
                # Checks if the guess is the same as the correct word
                if guess == word:
                    print("You guessed the correct word!")
                    print(f'\nCongratulations, you won the game! The word was "{word}"!')
                    break
                else:
                    # If the guess is not the same as the correct word, then increment the incorrect guess counter
                    print('Please enter another letter. Try again.')
                    incorrect_guesses += 1
            else:
                print('Good guess! The letter is in the word!')
                # Check if the player has won by guessing all the letters in the word
                if all(letter in guessed_letters for letter in word):
                    print(f'\nCongratulations, you won the game! The word was "{word}"!')
                    break
        else:
            # If the letter is not in the word and the letters is more than one character, increment the incorrect guess counter
            incorrect_guesses += 1
            print('Sorry, please try again.')

        remaining_chances = len(hanged_body)
        print(f'\nRemaining Chances: {remaining_chances - incorrect_guesses}')

        # Print the updated state of the game, with correctly guessed letters revealed
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

# If the player has run out of incorrect guesses, print a message and end the game
if incorrect_guesses == remaining_chances:
    print(full_body)
    print(f'\nSorry, you lost the game. The word was "{word}".')
