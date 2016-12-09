class Savings:
    """
    This grabs a savings account object based on the id inputted
    :param id: :
    :return:
    """
    account_list = []

    id = 0

    def __init__(self,first,last,initial_deposit):
        self.first = first
        self.last = last
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.interest = interest
        self.transactions_history = []


    def deposit(self,amount):
        self.balance += amount
        self.transactions_history.append("Deposited" + str(amount))

    def withdraw(self,amount):
        self.balance -= amount
        self.transactions_history.append("Withdrew" + str(amount))

    def apply_interest(self,amount)
        self.interest = int(self.interest * self.)
