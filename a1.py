import random
playing=True
number=str(random.randint(10,20))
print("I wll generate a number from 10 to 20,and you have to guess the number one digit at a time ")
print("The guess ends when you get 1 hero!")

while playing:
    guess=input("Give me your best guess!\n")
    if number==guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("Your guess isn't quite right,try again.\n ")