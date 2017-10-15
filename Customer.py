from Account import Account

class Customer:
    def __init__(self, username, balanceid, f, l, amt):
        self.__account_init = Account(amt)
        self.__username = username
        self.__balanceid = balanceid
        self.__firstName = str(f)
        self.__lastName = str(l)
        self.__account = {username: {"BALANCE ID: ": self.__balanceid,
                                     "NAME: ": self.__firstName + " " + self.__lastName,
                                     "BALANCE:": self.__account_init.getBalance(balanceid)}}

    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getAccount(self, username):
        return self.__account[username]
    def createAccount(self, username, balanceid, f, l, balance):
        self.__account_init.newAcc(balanceid, balance)
        self.__account[username] = {"BALANCE ID: ": balanceid,
                                    "NAME: ": f + " " + l,
                                    "BALANCE:": self.__account_init.getBalance(balanceid)}
    def editBalanceDeposit(self, username, balanceid, amt):
        self.__account_init.deposit(balanceid, amt)
        self.__account[username]["BALANCE:"] = self.__account_init.getBalance(balanceid)
    def editBalanceWithdraw(self, username, balanceid, amt):
        self.__account_init.withdraw(balanceid, amt)
        self.__account[username]["BALANCE:"] = self.__account_init.getBalance(balanceid)
    def editForeignDeposit(self, balanceid, amt):
        self.__account_init.deposit(balanceid, amt)
