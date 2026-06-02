# bank class
# username, acc no, acc balance
# acc deposit, acc withdrawl, acc balance check, acc info check

# param - amount -> self.acc_bal + amount
# param - amount -> self.acc_bal - amount

class Bank:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        self.acc_bal = 0

    def check_bal(self):
        print(f"Account balance : {self.acc_bal}")

    def check_info(self):
        print(f"Name: {self.name}, Account Number: {self.acc_no}, Account balance : {self.acc_bal}")

    def deposit(self, amount):
        self.acc_bal += amount
        print("Credited successfully")

    def withdraw(self, amount):
        if(self.acc_bal >= amount):
            self.acc_bal -= amount
            print("withdrawl successful")
        else:
            print("not enough money!! gareeb")

user1 = Bank("Mohit", 1234)

user1.check_info()
user1.deposit(1000)
user1.check_bal()

user1.withdraw(1000)
user1.check_bal()