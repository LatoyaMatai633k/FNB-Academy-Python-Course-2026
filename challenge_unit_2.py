def secure_password():
    secret_password = input("Enter your secret password: ").strip()
    hint = f"Your passwrd hint: your password starts with {secret_password[0]} and ends with {secret_password[-1]}"

    print(hint)

secure_password()