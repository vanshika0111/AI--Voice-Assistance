while True:
    print("Press q to quit.")
    a = input("Enter a digit: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
            print("You entered number greater than 6.")
    except Exception as e:
        print(f"Your input resulted in error: {e}")

print("Thanks!")