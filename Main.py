from Bank import Bank
import random
bank = Bank("", "", "", "", 0)
def main():
    print("===========================\n"
          "   INTERCONTINENTAL BANK   \n"
          "===========================\n")
    while True:
        print("      MAIN MENU   \n"
              "   --------------\n")
        mainAction = input("[1] ADD NEW CUSTOMER\n"
                           "[2] SHOW NUMBER OF CUSTOMERS\n"
                           "[3] LOGIN\n"
                           "[4] EXIT\n")
        if mainAction == "1":
            userName = input("ENTER NEW USERNAME: ")
            if bank.getCustomerList(userName) == False:
                balanceId = random.randrange(0, 10000000)
                print("YOUR BALANCE ID IS: ", balanceId)
                firstName = input("ENTER FIRST NAME: ").upper()
                lastName = input("ENTER LAST NAME: ").upper()
                initBalance = int(input("ENTER STARTING BALANCE: "))
                bank.addCustomer(userName, balanceId, firstName, lastName, initBalance)
                print("NEW CUSTOMER ADDED\n")
            else:
                print("CUSTOMER ALREADY EXIST\n")
        if mainAction == "2":
            print(bank.getNumofCustomers())
        if mainAction == "3":
            userName_inp = input("INPUT USERNAME: ")
            if bank.getCustomerList(userName_inp) == True:
                while True:
                    user_dict = bank.getCustomer(userName_inp)
                    user_list = list(user_dict.values())
                    user_balanceId = user_list[0]
                    balance = user_list[2]

                    subAction = input("\n"
                                      "[1] DEPOSIT\n"
                                      "[2] WITHDRAW\n"
                                      "[3] TRANSFER\n"
                                      "[4] SHOW BALANCE\n"
                                      "[5] ACCOUNT DETAILS\n"
                                      "[6] EXIT TO MAIN MENU\n")
                    if subAction == "1":
                        deposit = int(input("ENTER AMOUNT: "))
                        if deposit > 0:
                            bank.editCustomerDeposit(userName_inp, user_balanceId, deposit)
                        else:
                            print("ENTER A LARGER NUMBER\n")
                    if subAction == "2":
                        withdraw = int(input("ENTER AMOUNT: "))
                        if withdraw <= balance:
                            bank.editCustomerWithdraw(userName_inp, user_balanceId, withdraw)
                        else:
                            print("BALANCE NOT ENOUGH\n")
                    if subAction == "3":
                        transfer = int(input("ENTER AMOUNT: "))
                        destination = int(input("DESIGNATED ACCOUNT BALANCE ID: "))
                        bank.editForeignDeposit(destination, transfer)
                        bank.editCustomerWithdraw(userName_inp, user_balanceId, transfer)

                    if subAction == "4":
                        print("BALANCE: ", balance, "")
                    if subAction == "5":
                        for items in user_dict.items():
                            print(items)
                    if subAction == "6":
                        break
        if mainAction == "4":
            print("===========================\n"
                  "   INTERCONTINENTAL BANK   \n"
                  "===========================\n")

            break


main()
