class Soda_Machine:
    def __init__(self, name, paid, balance):
        self.name = name
        self.paid = paid
        self.balance = balance

    def eject_soda(self):
        if self.paid == False:
            print("Please insert money")
        else:
            print("Enjoy the soda")
        return self


class Customer(Soda_Machine):
    def __init__(self, name, paid, balance, amount):
        super().__init__(name, paid, balance)
        self.amount = amount

    def pay(self, amount):
        self.balance -= amount
        print(f"{self.balance}$")
        return self

    def select_soda(self):
        if self.balance >= 1:
            self.paid = True
            self.balance -= 1
        else:
            self.paid = False
        return self


sprite = Soda_Machine("Sprite", 30, 20)
customer = Customer(30, 20, 80, 50)
customer.pay(50)
print(sprite.eject_soda().paid)
print(customer.select_soda().paid)