import random


def main():
    eqn = 10
    score = 0
    lvl = get_level()

    while eqn > 0:
        x, y = generate_integer(lvl), generate_integer(lvl)
        chances = 3
        answer = x + y
        while chances > 0:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                chances -= 1

        if chances == 0:
            print(f"{x} + {y} = {answer}")

        eqn -= 1

    print(f"Score: {score}")




def get_level():
    level = -1
    while not (level == 1 or level == 2 or level == 3):
        try:
            level = int(input("Level: "))
        except ValueError:
            level = -1
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
    else:
        x = random.randint(100,999)
    return x


if __name__ == "__main__":
    main()

