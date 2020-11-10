import random

"""
Hangman game
pulls common words from a file, puts in list
randomly chooses words
starts game, prompts user for guess, 5 guesses
if guess right = can guess wrong
if guess wrong = guess again
after 5 guesses = win or lose
can choose to play again
"""

#pulls word list, into list
def pull_words():
    f = open("/Users/ianyuen/Documents/GitHub/mpcs50101-2020-autumn-assignment-4-pirateontheseas/common_words.txt", "r")
    global word_list
    word_list = []
    
    for i in f:
        x = i.strip()
        y = x.lower()
        word_list.append(y)
    
    f.close 

    return(word_list)


#randomly choose a word
def choose_word():
    global word_list
    top = len(word_list)
    number = random.randrange(0, top)
    global chosen_word

    #minus 1 as index start at 0
    chosen_word = word_list[number-1]

    return 0

#takes guess, checks guess, prompts message_center
def take_guess(y):

    global theguess
    theguess = y.lower()

    global right_guess_counter

    global guess_counter

    global guess_right

    global chosen_word
    

    for i in range(0, (len(chosen_word))):
        if chosen_word[i] == theguess:
            right_guess_counter += 1
            guess_right.append(chosen_word[i])
            message_center(1)
            break
        elif chosen_word[i] != theguess and i == (len(chosen_word)-1):
            guess_counter += 1
            message_center(0)
            break
    
    return 0

#when prompted with value from take_gues() and take_word_guess() returns appropriate message to users
def message_center(y):

    global message1

    global message2

    global theguess

    global guess_counter

    if y == 0:
        message1 = str(theguess) + " is not in the word. \n" + "You have " + str(5 - guess_counter) + " guesses reamining."
        print(message1)
        
        if (5 - guess_counter) > 0:
            prompt_guess()
        elif (5 - guess_counter) == 0:
            print("You lost! \n" + "The word was " + chosen_word.upper())
            play_again()

    if y ==1:
        message2 = theguess + " is in the word" + the_display(guess_right)
        print(message2)
        guess_word()
  
    if y == 2:
        message3 = "Congratulations! \n" + "The word was " + chosen_word.upper()
        print(message3)
        play_again()
    return 0

#takes word guessed as argument, returns message, prompts the subsequent step
def take_word_guess(y):
    global chosen_word

    if y == chosen_word:
        message_center(2)
    else:
        print("That is not the word")
        if guess_counter < 5:  
            prompt_guess()
        elif guess_counter ==5:
            print("You lost! \n" + "The word was " + chosen_word.upper())
            play_again()


#prompts guess, takes input, checks input, calls take_guess to verify guess
def prompt_guess():
    print("Guess a letter?")
    x = input()
    #makes sure it is one letter/alphabet guess
    if len(x) > 1:
        print("One alphabet only please. Try again.")
        prompt_guess()
    
    take_guess(x)

    return 0

#prompts guess a word, takes input, checks input, calls take_word_guess to verify guess
def guess_word():
    print("Try and guess the word?")
    x = input()
    take_word_guess(x)

    return 0


#function that takes argument guess_right, a list of alphabets guessed right by user
#evaluates this in relation to chosen_word, to display visualization of what parts of words guessed right
#returns ths display as a string , for when take_guess determines a right answer
def the_display(y):
    
    global chosen_word
    global right_guess_counter

    aa = len(chosen_word)

    display_list =[]
    number_list = []
    
    global display
    display = " "
    
    #recursive, gets letter positions gussed right by user
    
    for i in range(len(chosen_word)):
        number_list.append(i)
        for j in range(len(guess_right)):
            if chosen_word[i] == guess_right[j]:
                display_list.append(i)
    
    use_list = sorted(display_list)
    
    #generates the cisualization, recursively, by comparing number list representing index of chosen_word
    #compared against result of above recursion, 
    def generate(a, b):
        global display
        if bool(a) == False and bool(b) ==False:
            return 0
        
        if bool(a) == False and bool(b) ==True:
            display += ("_ ")
            return generate(a, b[1:])

        if a[0] == b[0]:
            display += (chosen_word[a[0]]+ " ")
            return generate(a[1:], b[1:])
        
        if a[0] != b[0]:
            display += ("_ ")
            return generate(a, b[1:])
    
    #calling above function
    generate(display_list, number_list)
     

    return display

# play again
def play_again():
    print("Would you like to play again? (y/n)")
    x = str(input())

    if x[0] == "y":
        start_game()
    else:
        exit()

#main game command center

def start_game():
    #initializing global variables
    global theguess
    theguess = ""

    global right_guess_counter
    right_guess_counter = 0

    global guess_counter
    guess_counter = 0

    global guess_right
    guess_right =[]

    global chosen_word
    chosen_word = ""

    global message1
    message1 = "" 

    global message2
    message2 = ""

    global display

    #generating the word
    pull_words()
    choose_word()
    
    #prompts to begin game
    #tried best to replicate specified emoji
    print("Let's Play Hangman  ̄\_(''/)_/ ̄)")
    print(" ")
    prompt_guess()

    

#boiler-plate code
def main():
    start_game()


if __name__ == '__main__':
    main()
