from Customer import Customer
class Bank:
    def __init__(self, username, balanceid, f, l, balance):
     self.__customeracc = Customer(username,balanceid, f, l, balance)
     self.__customers = []

    def addCustomer(self, username, balanceid, f, l, balance):
     self.__customeracc.createAccount(username, balanceid, f, l, balance)
     self.__customers.append(username)

    def editCustomerDeposit(self, username, balanceid, amt):
     self.__customeracc.editBalanceDeposit(username, balanceid, amt)

    def editForeignDeposit(self, balanceid, amt):
     self.__customeracc.editForeignDeposit(balanceid, amt)

    def editCustomerWithdraw(self, username, balanceid, amt):
     self.__customeracc.editBalanceWithdraw(username, balanceid, amt)

    def getCustomerList(self, username):
     return self.__customers.count(username)

    def getNumofCustomers(self):
     return len(self.__customers)

    def getCustomer(self, username):
     return self.__customeracc.getAccount(username)
