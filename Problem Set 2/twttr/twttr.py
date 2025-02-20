vowels = ['A', 'a', 'E', 'e', 'U', 'u', 'I', 'i', 'O', 'o']
str = input("Input: ")
answer = ""

for char in str:
    if char in vowels:
        continue
    answer += char

print("Output:", answer)
