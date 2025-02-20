greet = input("Greeting: ")

if "hello" in greet.lower():
    print("$0")
elif greet.lower().startswith('h'):
    print("$20")
else:
    print("$100")
