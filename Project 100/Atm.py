class ATM:
    def __init__(self, cardNumber, pinNumber, money):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.money = money

def main():
    User = ATM(1234678910, 1234, money = '')
    User.money = "1000000000"
    pin = User.pinNumber
    
    def remain():
        def cashWithdrawal():
            cashAmt = input("How much money do you want to withdraw?(this has to be a number): ")
            if(int(cashAmt) == 1):
                rightWord = "has"
            else:
                rightWord = "have"
            if(int(cashAmt)==0):
                print("this action cannot be performed - pls try again")
                cashWithdrawal()  
            if(int(cashAmt)/int(cashAmt) == -1 or int(User.money)-int(cashAmt) <=-1 ):
                print("this action cannot be performed - pls try again")
                cashWithdrawal()
            elif(int(cashAmt)/int(cashAmt) == 1 or int(User.money)-int(cashAmt)>=0):
                print("$"+cashAmt+" "+rightWord+" been withdrawn from your account")
                User.money = str(int(User.money)-int(cashAmt))
    
        def balanceEnquiry():
            print("Alright. Your balance is "+User.money)
            ulState = input('To use our system again, type *yes*. If you dont do so, an error will show. ')
            if(ulState == "yes"):
                remain()
            else:
                "Error. Run program again to try again"

        def cashDep():
            deppedCash = input("How much money do you want to deposit?(this has to be a number): ")
            if(int(deppedCash) == 1):
                rightWord = "has"
            else:
                rightWord = "have"
        
            if(int(deppedCash)/int(deppedCash) == 1 or int(User.money)/int(deppedCash)>0):
                print("$"+str(deppedCash)+" "+rightWord+" been deposited into your account")
                User.money = str(int(User.money)+int(deppedCash))
            else:
                print('this action cannot be performed')

        pinCheck = input("Welcome back to the Exoticc bank, to continue, enter you pin: ")
        if(int(pinCheck) != pin):
            print("Your pin is not correct, pls try again")
            remain()
        else:
            print("Your pin is correct. Consider the following:")
            q1 = input("Do you want to withdraw any money? Reply w/ y/n: ")
            if(q1 == "y"):
                cashWithdrawal()
            elif(q1 == "n"):
                print("Alright")
            elif(q1 != "y" and q1 != "n"):
                print('you did not reply with y or n - try again')
                q1 = input("Do you want to withdraw any money? Reply w/ y/n: ")
                if(q1 == "y"):
                    cashWithdrawal()
                elif(q1 == "n"):
                    print("Alright")
                elif(q1 != "y" and q1 != "n"):
                    print('you did not reply with y or n again - let us move on')
        
            q2 = input("Do you want to deposit any money? Reply w/ y/n: ")
            if(q2 == "y"):
                cashDep()
            elif(q2 == "n"):
                print("Alright")
            elif(q2 != "y" and q2 != "n"):
                print('you did not reply with y or n - try again')
                q2 = input("Do you want to deposit any money? Reply w/ y/n: ")
                if(q2 == "y"):
                    cashDep()
                elif(q2 == "n"):
                    print("Alright")
                elif(q2 != "y" and q1 != "n"):
                    print('you did not reply with y or n again - let us move on')
        
            q3 = input("Do you want to know your balance? reply w/ y/n: ")
            if(q3 == "y"):
                balanceEnquiry()
            elif(q3 == "n"):
                print("Alright. Thank you for using the Exoticc bank")
            elif(q3 != "y" and q3 != "n"):
                print('you did not reply with y or n - try again')
                q3 = input("Do you want to know your balance? Reply w/ y/n: ")
                if(q3 == "y"):
                    balanceEnquiry()
                    print("Thank you for using the Exoticc bank online system")
                elif(q3 == "n"):
                    print("Alright. Thank you for using the Exoticc bank online system")
                elif(q3 != "y" and q1 != "n"):
                    ulState = input('you did not reply with y or n again. Thank you for using Exoticc bank. To try again, type *yes*. If you dont do so, an error will show ')
                    if(ulState == "yes"):
                        remain()
                    else:
                        "Error. Run program again to try again"

main()