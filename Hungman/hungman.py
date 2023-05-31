import random
from words import words
import string

# print(words)
# make sure word generated to guess is valid 
def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    trials = 1
    
    while len(word_letters) > 0 and lives:
        print('You have used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('word is:',' '.join(word_list))
        print(f'you are on trial {trials}')
        print(f'You have {lives} lives left')


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('letter not in word')

        elif user_letter in used_letters:
            print('You have already used the character, try again')

        else:
            print('You have entered a none alphabet charater')

        if lives == 0:
            print('...............................')
            print(f'Out of lives...Need more lives')
            choice = input("Add lives? (y or n)")
            if choice.upper() == 'Y':
                lives = 6
                trials +=1
            else:
                break
        

    if lives == 0:
        print(f'You died!, the word was {word}')
    else:
        print(f'You geussed correctly {word}')


hangman()

    
