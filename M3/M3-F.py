##################
import random

def get_random_word(words):
    random_index = random.randrange(len(words))
    return words[random_index]
##################

import math

def get_player_guess():
    is_valid = False
    guess = input('Please enter your guess: ')
    while is_valid == False:
        if guess.isalpha() and len(guess)==5:
            is_valid = True
            return guess.lower()
        else:
            guess = input('Your guess must have 5 letters: ')

def play_round(word):
    is_correct = False
    guess_count = 1
    while is_correct == False:
        letter_list = ['_','_','_','_','_']
        print (f'Guess {guess_count}:\n')
        guess = get_player_guess()
        count = 0
        for i in guess:
            if i in word:
                if i == word[count]:
                    letter_list[count] = i.upper()
                else:
                    letter_list[count] = i.lower()
            count += 1

        #check
        count_letters_dict = {}
        for i in word:
            number = word.count(i)
            count_letters_dict[i] = number
        for i in letter_list:
            if i.isalpha():
                temp_up = i.upper()
                temp_down = i.lower()
                if (letter_list.count(temp_up)) + (letter_list.count(temp_down)) > (count_letters_dict[temp_down]):
                    index = len(letter_list)-1-letter_list[::-1].index(temp_down)
                    letter_list[index] = '_'
        
            
        #check
            
        print (' '.join(letter_list))
        print()
        if word == guess:
            is_correct = True
            return (guess_count, is_correct)
        if guess_count == 6:
            return (guess_count, is_correct)
        guess_count += 1

def get_words(filename):
    f = open(filename, 'r')
    lines = f.read().split()
    f.close()
    return (lines)

def print_bar_chart(data_dict):
    for key in sorted(data_dict.keys()):
        print (f'{key}|', end = '')
        print (('#'*data_dict[key]) + str(data_dict[key]))

def intro():
    filename = input ('Enter the name of the word file: ')
    name = input ('Please enter your name: ')
    print ()
    print (f'Welcome to Wordle 101 {name}')
    print ()
    print ('='*72)
    print ('                                 Rules\nYou have 6 guesses to figure out the solution.\nAll solutions are words that are 5 letters long.\nWords may include repeated letters.\nLetters that have been guessed correctly are displayed in uppercase.\nLetters that are in the word but have been guessed in the wrong location\nare displayed in lowercase.')
    print ('='*72)
    print ()
    return filename

def print_ending(word, guess_count, is_correct):
    cont = None
    if (is_correct):
        print (f'Success! The word is {word}!\n')
    else:
        print (f'Better luck next time! The word is {word}!\n')
    while (cont != 'Y' and cont != 'N'):
        cont = input ('Please enter \'Y\' to continue or \'N\' to stop playing: ')
        if (cont != 'Y' and cont != 'N'):
            print ('Only enter \'Y\' or \'N\'!')
    if (cont == 'N'):
        return False
    else:
        return True

def play_game(filename):
    round_count = 1
    outcome_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    word_list = get_words(filename)
    winrate = 0
    wins = 0
    cont = True
    while cont == True:
        print ()
        print (f'Round: {round_count}\n')
        word = get_random_word(word_list)
        round_tuple = play_round(word)
        if (round_tuple[1] == True):
            outcome_dict[round_tuple[0]] += 1
            wins += 1
        cont = print_ending(word, round_tuple[0], round_tuple[1])
        winrate = math.ceil((float(wins)/float(round_count))*100)
        round_count += 1
    print ()
    print ('='*72)
    print ('                                Summary')
    print (f'Win percentage: {winrate}%')
    print ('Win Distribution:')
    print_bar_chart(outcome_dict)
    print ('='*72)
        

def main():
    filename = intro()
    play_game(filename)


main()
