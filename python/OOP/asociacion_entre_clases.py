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


class User:
    def __init__(self, name, email, accounts_list):
        self.name = name
        self.email = email
        self.accounts = accounts_list

    def make_deposit(self, account_index, amount):
        self.accounts[account_index].deposit(amount)
        return self

    def make_withdrawal(self, account_index, amount):
        self.accounts[account_index].withdraw(amount)
        return self

    def display_user_balance(self):
        print("Usuario: " + self.name)
        for i in range(1, len(self.accounts) + 1):
            print("\tCuenta " + str(i) + ":\n\t\tSaldo: $" + str(self.accounts[i - 1].balance))
        return self

    def transfer_money(self, account_index1, other_user, account_index2, amount):
        self.accounts[account_index1].balance -= amount
        other_user.accounts[account_index2].balance += amount
        return self

    def yield_int(self):
        for acc in self.accounts:
            acc.yield_interest()
        return self


# Crea 2 cuentas para usuario 1
account1 = BankAccount(0.01, 100)
account2 = BankAccount(0.03)
user1 = User("USER1", "user1@mail.com", [account1, account2])

# Crea 3 cuentas para usuario 2
account3 = BankAccount(0.01, 100)
account4 = BankAccount(0.02, 200)
account5 = BankAccount(0.03)
user2 = User("USER2", "user2@mail.com", [account3, account4, account5])

# En la primera cuenta del usuario 1, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la
# información de la cuenta en una sola línea de código (es decir, encadenamiento)
user1\
    .make_deposit(0, 20)\
    .make_deposit(0, 200)\
    .make_deposit(1, 120)\
    .make_withdrawal(0, 100)\
    .yield_int()\
    .display_user_balance()

# En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la
# cuenta en una sola línea de código (es decir, encadenamiento)
user2.make_deposit(0, 100)\
    .make_deposit(1, 30)\
    .make_withdrawal(2, 10)\
    .make_withdrawal(0, 20)\
    .make_withdrawal(1, 30).yield_int()\
    .display_user_balance()
