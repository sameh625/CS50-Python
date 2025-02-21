grocery = {}
while True:
    try:
        item = input().upper()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] +=1
    except EOFError:
        for things in sorted(grocery):
            print(f"{grocery[things]} {things}")
        break

