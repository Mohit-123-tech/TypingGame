from random import sample
from colorama import Fore
from playsound import playsound
from sys import platform
from os import system

NumberList = "12345678910"
AlphaList = "abcdefghijklmnopqrstuvwxyz"
points = 0

if __name__ == "__main__":
    
    # check platform to clear console [Windows & Linux]
    if platform.__str__() == "windows":
        system("cls")
    else:
        system("clear")

    lenght = input("Enter Lenght For Word : ") # get Word Length from user

    try:
        lenght = int(lenght)
    except (Exception):
        print(Fore.RED, "Enter Valid Value", Fore.WHITE)
        exit() 

    while(True):
        all = NumberList+AlphaList

        # Make random words By lenght 
        word = ''.join(sample(all, lenght))
        print(word+"\n")

        # Word Entered by user
        print(Fore.GREEN, "Enter q to quit", Fore.WHITE)
        userWord = input("Type Word : ")

        if word == userWord:
            print(Fore.GREEN, "okay", Fore.WHITE)
            points += 5

        elif userWord == 'q':
            print(f"Your Points is : {points}")
            break

        else:
            print(Fore.RED, "Try Again", Fore.WHITE)
            points -= 1
            # play sound after user entered wrong word
            playsound("sound/gameOver.mp3")

