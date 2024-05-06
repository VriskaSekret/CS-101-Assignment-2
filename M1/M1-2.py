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
        
play_round("ghost")
