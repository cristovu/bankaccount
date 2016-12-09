class Checking:
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
        self.transactions_history = []

        Checking.id += 1

    def deposit(self,amount):
        self.balance += amount
        self.transactions_history.append("Deposited " + str(amount))

    def withdraw(self,amount):
        self.balance -= amount
        self.transactions_history.append("Withdrew " + str(amount))

"""
    def memeber(self):

        return '{} {} {}'.format(self.frist,self.last, )


    def deposit(self,amount):
        self.balance += amount
        self.trans_history.append("Deposited: " + str(amount))

    def withdraw(self,amount):
        self.balance -= amount
        self.trans_history.append("Withdrew: " + str(amount))

    def transfer_to_savings(self,amount,savings):
        self.balance -= amount
        self.trans_history.append("Transferred: " + str(amount))
        savings.balance += amount
        savings.trans_history.append("Received Transgers " + str(amount))


    def transfer_to_member(self,amount,from,to):
        self.balance -= amount
        self.trans_history.append("Transferred: " + str(amount))
        Account.id += amount
        savings.trans_history.append("Received Transfers " + str(amount))

    def __repr__(self):
        return int(self.idnum)

    def print_trans_history(self):

        for i in self.trans_history
"""
