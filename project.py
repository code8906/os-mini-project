while True:
    print("\n----- MENU -----")
    print("1. Add Numbers")
    print("2. Check Even or Odd")
    print("3. Find Factorial")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == "2":
        num = int(input("Enter number: "))
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    elif choice == "3":
        n = int(input("Enter number: "))
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial =", fact)

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid choice, try again")
