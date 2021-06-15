class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.balance -= 5
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Saldo: $" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate
        return self


# Crea 2 cuentas
account1 = BankAccount(0.01, 100)
account2 = BankAccount(0.03)

# En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la información de la
# cuenta en una sola línea de código (es decir, encadenamiento)
account1.deposit(20).deposit(200).deposit(120).withdraw(300).yield_interest().display_account_info()

# En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la
# cuenta en una sola línea de código (es decir, encadenamiento)
account2.deposit(100).deposit(30).withdraw(10).withdraw(80).withdraw(50).yield_interest().display_account_info()
