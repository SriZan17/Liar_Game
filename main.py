import random
import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_console()
    print("Welcome to the Liar Game!")
    print("==========================")
    print("Enter the number of players: ")

    no_of_players = int(input())
    imposter = random.randint(1, no_of_players - 1)
    current_player = 1
    print("Player 1's turn")
    print("Enter the word to be guessed and announce its category: ")
    word = input()

    clear_console()
    print("The game is starting!")
    print("=====================")

    while current_player < no_of_players:
        clear_console()
        print(f"Player {current_player+1}'s turn")
        input("Press enter to reveal the word...")

        if current_player == imposter:
            print("You are the Liar!")
        else:
            print(f"The word is: {word}")

        input("Press enter to continue...")
        current_player += 1

    clear_console()
    print("Game Start!")
    print("==========")


if __name__ == "__main__":
    main()
