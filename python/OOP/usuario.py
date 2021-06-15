class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # agrega el método deposit
    def make_deposit(self, amount):	 # toma un argumento que es el monto del depósito
        self.account_balance += amount  # la cuenta del usuario específico aumenta por la cantidad del valor recibido

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("Usuario: " + self.name + ", Saldo: " + str(self.account_balance))

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


# Crea tres instancias de la clase usuario
user1 = User("USER1", "user1@mail.com")
user2 = User("USER2", "user2@mail.com")
user3 = User("USER3", "user3@mail.com")

# Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
user1.make_deposit(100)  # account_balance = 100
user1.make_deposit(350)  # account_balance = 450
user1.make_deposit(1050)  # account_balance = 1500

user1.make_withdrawal(500)  # account_balance = 1000

user1.display_user_balance()

# Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
user2.make_deposit(300)  # account_balance = 300
user2.make_deposit(800)  # account_balance = 1100

user2.make_withdrawal(250)  # account_balance = 850
user2.make_withdrawal(150)  # account_balance = 700

user2.display_user_balance()


# Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
user3.make_deposit(900)  # account_balance = 900

user3.make_withdrawal(200)  # account_balance = 700
user3.make_withdrawal(100)  # account_balance = 600
user3.make_withdrawal(150)  # account_balance = 450

user3.display_user_balance()


# BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y
# luego imprima los saldos de ambos usuarios
user1.transfer_money(user3, 200)  # user1.account_balance = 800; user2.account_balance = 650
user1.display_user_balance()
user3.display_user_balance()
