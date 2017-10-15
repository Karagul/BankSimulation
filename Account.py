class Account:
    def __init__(self, balance):
        self.__balance = float(balance)
        self.__balancedict = {"": 0}

    def getBalance(self, balanceid):
        return self.__balancedict[balanceid]

    def newAcc(self, balanceid, amt):
        self.__balancedict[balanceid] = amt

    def deposit(self, balanceid, amt):
        self.__balancedict[balanceid] = self.__balancedict[balanceid] + float(amt)

    def withdraw(self, balanceid, amt):
        self.__balancedict[balanceid] = self.__balancedict[balanceid] - float(amt)
