import random

n = random.randint(1,9)
chance = 1
flag = 0
restart = "nothing"

print("You will get 5 chances to guess the number.")

while chance <= 5 and flag == 0:

    usern = int(input("Guess the number: "))

    #if usern != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    #   print("Please write a number from 1 to 9 (your chances are getting deducted)")

    if usern > n:
        print("The number is less than",usern)
        chance = chance+1

    if usern < n:
        print("The number is greater than",usern)
        chance = chance+1

    if usern == n:
        flag = 1
        print("OMG YOU WON!!!")
        chance = 7

    if chance == 6:
        print("You have exausted your chances")
        print("Game Over")
        restart = input("If you want to restart with a new number, type r: ")
        print(restart)

    if chance ==7:
        restart = input("If you want to restart with a new number, type r: ")
        print(restart)

    if restart == "r":
        print("You will get 5 chances to guess the number")
        flag = 0
        chance = 1
        restart = "nothing"
        n = random.randint(1,9)