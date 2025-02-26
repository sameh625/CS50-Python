def main():
    str = input("Input: ")
    ans = shorten(str)
    print("Output:",ans)


def shorten(word):
    vowels = ['A', 'a', 'E', 'e', 'U', 'u', 'I', 'i', 'O', 'o']
    answer = ""

    for char in word:
        if char in vowels:
            continue
        answer += char

    return answer

if __name__ == "__main__":
    main()
