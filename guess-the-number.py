# template for "Guess the number" mini-project
import simplegui
import random

# input will come from buttons and an input field
# all output for the game will be printed in the console
secret_number = -1
guesses_left = -1
max_range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guesses_left
    if max_range == 100:
        secret_number = random.randrange(0, 100)
        guesses_left = 7
    else:
        secret_number = random.randrange(0, 1000)
        guesses_left = 10
    print ""
    print "New Game. Range is from 0 to", max_range
    print "Number of remaining guesses is", guesses_left


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_range
    max_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_range
    max_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global guesses_left
    guess = int(guess)
    guesses_left -= 1
    print ""
    print "Guess was", guess
    print "Number of remaining guesses is", guesses_left
    if guess == secret_number:
        print "Correct!"
        new_game()
    else:
        if guesses_left > 0:
            if guess > secret_number:
                print "Lower!"
            elif guess < secret_number:
                print "Higher!"
        else:
            print "You lost! The number was", secret_number, "."
            new_game()
    

# create frame
frame = simplegui.create_frame("Guess the Number", 300, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)
frame.add_input("Enter your Guess", input_guess, 150)

# call new_game 
frame.start()
new_game()


# always remember to check your completed program against the grading rubric
