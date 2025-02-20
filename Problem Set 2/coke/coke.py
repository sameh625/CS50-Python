Amount = 50
valid = [5, 10, 25]

while Amount > 0:
    print (f"Amount Due: {Amount}")
    coin = int(input("Insert Coin: "))
    if coin in valid:
        Amount -= coin
    else:
        continue

print ("Change Owed:", (-1 * Amount))

