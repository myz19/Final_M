class naughtyException(Exception):
    def __init__(self, value):
        self.value = ["the cops are en route!!"]

    def __str__(self):
        return repr(self.value)

class Account:
    numMade = 0
    def __init__(self):
        self.__balance = 0      # balance is private
        self.accNo = Account.numMade + 1000
        Account.numMade += 1

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount):
        self.__balance = amount

    def spend(self, amount):
        print("please enter your account number")
        num = input()
        try:
            if int(num) == self.accNo:
                self.__balance -= amount
            else:
                # print("the cops are en route!!")
                raise naughtyException("bad stuff")
        except naughtyException as nE:
            print(nE)

    def deposit(self, amount):
        self.__balance += amount

mine = Account()
mine.setBalance(2000)
mine.spend(4000)
print("my balance = " + str(mine.getBalance()))
