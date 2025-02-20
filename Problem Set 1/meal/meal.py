
def main():
    time = input("What time is it? ")

    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")

    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")

    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes  = time.split(":")
    hours = int (hours)
    minutes = float (minutes) / 60
    return float(hours + minutes) 


if __name__ == "__main__":
    main()
