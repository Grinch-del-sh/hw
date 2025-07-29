num = 190

if num == 0:
    print("zero number")
else:
    prefix = "positive" if num > 0 else "negative"
    if num % 2 == 0:
        print(f"{prefix} even number")
    else:
        print(f"{prefix} odd number")
        print("number is not even")