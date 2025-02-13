import random
import time, sys

def slow_print(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

question = ("What color is player")
colors = ["green", "blue", "orange", "white", "purple"]
direction = ["left", "right", "top left", "bottom left", "top right", "bottom right"]
invalid = ("Not a valid input.")

while True:
    start = input("Start? (y,n): ")

    if start == "y":
        while True:
            player1 = input(f"{question} 1?: ")
            if player1 in colors:
                break
            else:
                print(invalid)

        while True:
            player2 = input(f"{question} 2?: ")
            if player2 in colors:
                break
            else:
                print(invalid)

        slow_print("....")

        slow_print(f"{player1} is on top, {player2} is under.", delay=.04)

        slow_print("....")

        slow_print("S..L..A..M!!!!",delay=.03)

        slow_print("....")

        victim = random.choice([player1, player2])
        position = random.choice(direction)

        slow_print(f"{victim} will move:", delay=.04)

        slow_print("....")

        slow_print("Getting Direction.", delay=.04)

        slow_print("....")

        slow_print(f"{position} 1 space.", delay=.04)

        slow_print("....", delay=.1)

        continue

    elif start == "n":
        break

    else:
        print("Start? (y,n): ")

print("Slamming Stopped")


