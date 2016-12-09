class Account:
    """docstring for Account."""

    def __init__(self):
        self.checking = Checking(100)
        self.savings = Savings(0)
        self.balance = 100

    def transfer_from_checking_to_savings(self, amount):
        #subtract amount from balance of Checking
        self.checking.balance -= amount
        #add amount to balance of Savings
        self.savings.balance += amount
        self.transactions_history.append("Transferred: " + str(amount))
        self.savings.transactions_history.append("Received Transfers " + str(amount))
        Account.id += amount

    def transfer_from_savings_to_checking(self, amount):
        #subtract amount from balance of Savings
        self.checking.balance += amount
        #add amount to balance of Checking
        self.savings.balance -= amount
        self.transactions_history.append("Transferred: " + str(amount))
        self.checking.transactions_history.append("Received Transfers " + str(amount))
        Account.id += amount


    def transfer_to_member(self,other,amount):
        #other = checking()
        self.balance -= amount
        self.transactions_history.append("Transferred: " + str(amount))
        savings.transactions_history.append("Received Transfers " + str(amount))
        Account.id += amount
        other.checking

    def __repr__(self):
        return int(self.idnum)

a1 = Account(1000)
print(a1.checking.balance)
print(a1.savings.deposit(1000))
print(a1.transfer_from_checking_to_savings.)
