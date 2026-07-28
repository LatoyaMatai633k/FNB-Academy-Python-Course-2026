def bank_transaction():
    bank_balance = 500
    withdrawal = float(input("Enter amount you want to withdraw: "))

    if withdrawal <= bank_balance:
        remaining_balance = bank_balance - withdrawal
        print(f"Withdrawal successful! Remaining balance: R{remaining_balance}")
    elif withdrawal < 0:
        print("Invalid amount. You must withdraw more than R0")
    else:
        print("Declined. Insufficient funds")

bank_transaction()