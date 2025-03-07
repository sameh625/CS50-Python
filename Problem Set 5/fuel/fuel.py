def main():
    while True:
        try:
            percentage = convert(input())
        except:
            pass
        else:
            break
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split('/')
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return int(round((x / y) * 100))

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else
        return str(percentage)


if __name__ == "__main__":
    main()
