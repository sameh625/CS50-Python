import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        match = validators.email(s)
        if match:
            return "Valid"
        else:
            return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
