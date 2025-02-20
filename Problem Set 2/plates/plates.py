def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:

        if s[0].isalpha() == False or s[1].isalpha() == False:
            return False

        for i in range(len(s)):
            if s[i].isdigit() :
                if i == len(s) - 2 and s[i] == '0':
                    return False
                elif not (i == len(s) - 1 or i == len(s) - 2 ):
                    return False

        for char in s:
            if char in ['.', ' ', '!', '?']:
                return False

        return True
    else:
        return False



main()
