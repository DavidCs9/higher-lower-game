from sys import flags
from art import *
from help import data
import random
from replit import clear

clear()
def get_person():
    """
    Get a person from the data.
    """
    # Get a random person from the data.
    person = random.choice(data)
    return person

def print_person(person):
    """
    Print the person's name and description.
    """
    # Print the person's name and description.
    return (f'{person["name"]}, a {person["description"]}, from {person["country"]}')


#function to compare two person followers and return the winner
def compare_followers(person1, person2):
    if person1["follower_count"] > person2["follower_count"]:
        return 'a'
    else:
        return 'b'

#function to ask the user who has more followers and type a or b
def ask_user():
    user_input = input("Who has more followers? Type a or b: ")
    return user_input
def play_game():
    
    score = 0
    flag = True
    #get two random people
    person1 = get_person()
    person2 = get_person()
    right_person = person1
    while flag:
        clear()
        print(logo)
        print(f'Your score is {score}')
        if score > 0:
            person2 = get_person()
        print(f'Compare A: {print_person(right_person)}')
        print(vs)
        print(f'Compare B: {print_person(person2)}')
        
        #compare the two people
        winner = compare_followers(person1, person2)

        #ask the user who has more followers
        user_input = ask_user()

        #if the user has the right answer
        if user_input == winner:
            if user_input == 'a':
                right_person = person1
            else:
                right_person = person2
            score += 1
            
            
        #if the user has the wrong answer
        else:
            print(f'Wrong! The correct answer is {winner}, your final score is {score}')
            flag = False


#create while to ask the user if they want to play again
while True:
    play_game()
    user_input = input("Would you like to play again? Type y or n: ")
    if user_input == 'n':
        break