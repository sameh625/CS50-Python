while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            continue
        ans = round(x / y * 100)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break

if ans >= 99.0:
    print ("F")
elif ans <= 1.0:
    print("E")
else:
    print(f"{ans}%")
