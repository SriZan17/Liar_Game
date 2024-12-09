import random
import os


def main():
    print("Enter the number of players: ")
    no_of_players = int(input())
    imposter = random.randint(1, no_of_players - 1)
    current_player = 1
    print("Enter the word to be guessed: ")
    word = input()
    clear_console()
    print("Welcome to the liar game!")
    while current_player < no_of_players:
        clear_console()
        input("Press enter to reveal the word...")
        if current_player == imposter:
            print("You are the Liar!")
        else:
            print(word)
        input("Press enter to continue...")
        current_player += 1


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
