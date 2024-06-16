import random as r
import sys

def Guessing_Game():
    try:
        # secret number will change only 1 time for entire game
        secret_number = r.randint(1, 11)
        while True:
            # secret number will change every time i made my guess
            # secret_number = r.randint(1, 11)
            
            guess = input('Enter your guess: ')
            if guess.lower() == 'q':
                print('Quitting the game')
                sys.exit()
                
            guess = int(guess)
            if guess == secret_number:
                print('Hoo You guessed it Correct')
                break   
            elif guess > secret_number:
                print('Too High')
            else:
                print('Too Low')
                
    except (KeyboardInterrupt, EOFError):
         print('Exiting from the game See yaa!')
    except ValueError:
        print('You Can Only Enter The Guess As "Number".')
    
def main():
    guess_num = Guessing_Game()
    while True:
        try_again = input('Do You Want to Try again? ').lower()
        if try_again == 'y':
            Guessing_Game()
        else:
            print('Thanks for playing!')
            return guess_num

if __name__ == '__main__':
    main()