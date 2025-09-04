
contacts = {}

while True:
    print("--- Contact Book ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")

    choice = input("Choose an option 1-4: ")

    if choice == "1":
        name = input("Enter name: ")
        num = input("Enter phone number: ")
        contacts[name] = num
        print("Contact saved!")

    elif choice == "2":
        if contacts:
            print("\nContacts:")
            for name, num in contacts.items():
                print(name, ":", num)
        else:
            print("No contacts saved.")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
