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



	
round_results = play_round("wacca")
print(f"Number of guesses: {round_results[0]}, Is solved? {round_results[1]}")
