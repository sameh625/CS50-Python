deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

if deep.strip() == "42" or deep.lower().strip() == "forty two" or deep.lower().strip() == "forty-two":
    print ("YES")
else:
    print("NO")
