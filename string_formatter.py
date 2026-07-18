def string_formatter():
    first_name = input("What is your name: ")
    last_name = input("What is your surnane: ")
    short_bio = input("Bio: ")

    username = f"{first_name[0]}{last_name}"

    print(f"{first_name.title()} {last_name.title()}")
    print(short_bio.strip())
    print(len(short_bio))
    print(short_bio.replace("I am", "I'm"))

    print(f"Hello my name is {first_name.title()} {last_name.title()} and {short_bio} and my username is {username.lower()}.")

string_formatter()
