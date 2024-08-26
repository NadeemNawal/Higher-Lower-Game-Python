from art import logo, vs
from game_data import data
import random
import turtle
from turtle import clear

score = 0


# format the account data in printable format
def format_data(account):
    """takes account data and returns printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    """checks followers against users guess"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"  # return true or false


game_should_continue = True
account_b = random.choice(data)
print(logo)
# generate a randomchoice from data
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"compare B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    # check if user is right or wrong
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)  # response is either true or false
    # function for score keeping
    clear()
    print(logo)
    if is_correct:  # means if is_correct is true
        score += 1
        print(f"you are right! current score: {score}")

    else:
        game_should_continue = False
        print(f"sorry, that's wrong. final score: {score}")
