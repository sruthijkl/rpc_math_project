import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)

def show_menu():
    print("\n--- Math RPC Client Menu ---")
    print("1. magicAdd(a, b)")
    print("2. magicSubtract(a, b)")
    print("3. magicFindMin(a, b, c)")
    print("4. magicFindMax(a, b, c)")
    print("5. Show operation counters")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Choose an option (0-5): ")

    try:
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = proxy.magicAdd(a, b)
            print(f"Result: {a} + {b} = {result}")

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = proxy.magicSubtract(a, b)
            print(f"Result: {a} - {b} = {result}")

        elif choice == "3":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            c = int(input("Enter third integer: "))
            result = proxy.magicFindMin(a, b, c)
            print(f"Minimum of ({a}, {b}, {c}) is: {result}")

        elif choice == "4":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            c = int(input("Enter third integer: "))
            result = proxy.magicFindMax(a, b, c)
            print(f"Maximum of ({a}, {b}, {c}) is: {result}")

        elif choice == "5":
            counters = proxy.getCounters()
            print("Operation Counters:", counters)

        elif choice == "0":
            print("Exiting client.")
            break

        else:
            print("Invalid choice. Please try again.")

    except Exception as e:
        print("Error:", e)
