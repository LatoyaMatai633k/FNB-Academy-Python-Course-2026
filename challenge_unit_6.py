def contact_number():
    contacts = {
        "Yaya": "0821112222",
        "Thabo": "0832223333",
        "Sarah": "0843334444"
    }

    name = input("Enter the name of the friend you want to look up: ").title()

    if name in contacts:
        print(f"Found! {name}'s number is {contacts[name]}")
    else:
        print("Contact not found.")

contact_number()