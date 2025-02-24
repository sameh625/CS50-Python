import random

level = -1
while level <= 0:
    try:
        level = int(input("Level: "))
    except ValueError:
        level = -1

ran = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            pass
        elif guess == ran:
            print("Just right!")
            break
        elif guess < ran:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        pass
