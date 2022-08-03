class User:
    def __init__(self, name, age):
        self.name= name
        self.age=age
    def show_details(self):
        return f"Thank you, {self.age} years old, {self.name}"


class Bank(User):
    total_deposits= 0
    total_withdrawals= 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance= balance

    def show_info(self):
        return f"Hello {self.name}, you have {round (self.balance, 2)} in your bank account."

    def deposits(self):
        dp= float(input("How much money would you like to deposit {self.name}?"))
        print("Thank you for depoiting.")
        self.balance += dp
        total_deposits+=1
        return f"Your current balance is: {self.balance}"

    def withdrawals(self):
        wd= float(input("Enter the mount of money to be withdrawn: "))
        if self.balance<wd:
            print("Sorry, not enough money in your bank account.")
        else:
            print("Thank you for withdrawing.")
            self.balance -= wd
            total_withdrawal+=1
            
