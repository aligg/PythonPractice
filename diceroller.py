from random import randint

name = input("Welcome to the dice game, what's your name?")
answer = input("Hey there %s. In the dice game the rules are as follows: You get three turns total. If you roll a 1 you get 0 points and a 6 gets you 10 points. For all other rolls, the score matches the number on the dice. Are you ready to give the dice a roll? (y)es or (n)o?" % (name))

score = 0
total_score = 0
turns = 0

while answer.lower()[0] == "y" and turns < 3:
    output = randint(1, 6)
    if output == 6:
        score = 10
    elif output == 1:
        score = 0
    else:
        score = output
    total_score += score 
    turns = turns + 1
    print("You rolled a %d for a score of %d. Your total score is now %d and your total turns are %d" % (output,score, total_score, turns))
    print ("Do you want to roll again? y or n?")
    answer = input()
if answer.lower()[0] == "n" or turns == 3:
    if total_score >= 10:
        print("Okay see ya later %s! Your final total score was %d. This means you win the game! Congratulations!" % (name, total_score))
    else:
        print("Okay bye %s! Your final total score was %d, This means you lost the game. Don't be afraid to play again! Better luck next time." % (name, total_score))


