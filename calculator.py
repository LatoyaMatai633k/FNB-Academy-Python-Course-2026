def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"{a} + {b} = {round(a + b, 2)}")
    print(f"{a} - {b} = {round(a - b, 2)}")
    print(f"{a} x {b} = {round(a * b, 2)}")

    if b == 0:
        print("Can't divide by 0")
    else:
        print(f"{a} / {b} = {round(a / b, 2)}")     

    print(f"{a} // {b} = {round(a // b, 2)}")
    print(f"{a} % {b} = {round(a % b, 2)}")

calculator()