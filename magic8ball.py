import random

answerlist = ["Certainly", "If it rains today, perhaps", "Absolutely!", "I would bet my life on it",\
"very doubtful", "Without a doubt", "Most likely", "My sources say no", "Concentrate and ask again",\
"Reply hazy try again", "Most likely", "Does the queen of England hoot?!", "As surely as big dutch babies rise"]

print("I am the Magic 8 ball.")
gameon = input("Are you ready to play? y/n?")

while gameon == "y":
    question = input("What would you like to ask?")
    print(random.choice(answerlist))
    gameon = input("Would you like to ask again? y/n")
if gameon == "n":
    print("Okay bye!")