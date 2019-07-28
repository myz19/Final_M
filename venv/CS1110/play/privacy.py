class PrivateTest:
    def __init__(self, a, b):
        self.easy2see = a
        self.__password = ""
        self.__hard2see = b

    def set_password(self, pwd):
        silly_hash = ""
        for i in range(len(pwd)):
            if i % 2 == 0:
                silly_hash += "X"
            else:
                silly_hash += pwd[i]
        self.password = silly_hash

    def check_password(self, hope):
        silly_hash = ""
        for i in range(len(hope)):
            if i % 2 == 0:
                silly_hash += "X"
            else:
                silly_hash += hope[i]
        return silly_hash == self.password

    def show_password(self):
        print("The password = " + self.password)

    def get_easy(self):
        return self.easy2see

    def get_hard(self):
        hopeful = input("please enter your password")
        if self.check_password(hopeful):
            return self.__hard2see
        else:
            print("Sorry, you're not authorised to see this")
            return ("calling the NSA and GCHQ ....")


experiment = PrivateTest("obvious", "hidden_stuff")
experiment.set_password("mega-secret")

# print ("easy done directly = " + experiment.easy2see)
# print ("\teasy done via accessor = " + experiment.get_easy())
# print ("hard done directly = " + experiment.__hard2see)
print("\thard done via accessor = " + experiment.get_hard())
experiment.show_password()