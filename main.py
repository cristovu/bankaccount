from checking import Checking
from savings import Savings

"""
def get_account(id):

    if id < len(Account.account_list):
        return Account.account_list[id]
    else:
        return 'none'

"""

def get_account(id):
    """
    This grab an account object based on the id inpitted
    :param id: the id num of the account we are trying to generate_lower_bound:
    :return:  The account object if found else return  'none'
    """
    for i in Checking.checking_list:

        if i.__repr__() == id:
            return i

    return 'none'

def get_account(id):
    """
    This grab an account object based on the id inpitted
    :param id: the id num of the account we are trying to generate_lower_bound:
    :return:  The account object if found else return  'none'
    """
    for i in Savings.savings:

        if i.__repr__() == id:
            return i

    return 'none'

def test():
    '''
    account_1 = Account('John','Doe',5000)
    account_2 = Account('Test','User',1000)
    account_1.deposit(400)
    account_1.deposit(1000)
    print(get_account(0).trans_history)
    '''

def main():

    c1 = Checking('John','Doe',5000)


    print(c1.balance)
    c1.withdraw(200)
    print(c1.transactions_history)
    print(c1.balance)

    s1 = Savings('Test','User',1000)
    print(s1.balance)
    s1.withdraw(200)
    print(s1.transactions_history)
    print(s1.balance)

main()
