class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


VALID_AGE = 18
pin, balance, age = [int(x) for x in input().split(", ")]

while True:
    line = input().split("#")
    if line[0] == "End":
        break

    if line[0] == "Send Money":
        money, pin_code = int(line[1]), int(line[2])

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin_code != pin:
            raise PINCodeError("Invalid PIN code")

        if age < VALID_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")


    elif line[0] == "Receive Money":
        salary = int(line[1])

        if salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        salary_after_invest = salary * 0.5
        balance += salary_after_invest
        print(f"{salary_after_invest:.2f} money went straight into the bank account")
