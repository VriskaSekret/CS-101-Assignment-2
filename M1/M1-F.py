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
    while is_correct == False:
        letter_list = ['_','_','_','_','_']
        guess = get_player_guess()
        count = 0
        for i in guess:
            if i in word:
                if i == word[count]:
                    letter_list[count] = i.upper()
                else:
                    letter_list[count] = i.lower()
            count += 1
        print (' '.join(letter_list))
        print()
        if word == guess:
            is_correct = True
def intro():
    word = input ('Enter word to guess: ')
    print ()
    name = input ('Please enter your name: ')
    print ()
    print (f'Welcome to Wordle 101 {name}')
    print ()
    print ('='*72)
    print ('                                 Rules\nYou have unlimited guesses to figure out the solution.\nAll solutions are words that are 5 letters long.\nLetters that have been guessed correctly are displayed in uppercase.\nLetters that are in the word but have been guessed in the wrong location\nare displayed in lowercase.')
    print ('='*72)
    print ()
    return word
    
def main():
    word = intro()
    play_round(word)

    
main()
