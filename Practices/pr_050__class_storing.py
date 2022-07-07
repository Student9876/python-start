#WAP a class programmer for storing information of few programmars working at microsoft 

from threading import get_ident


class Programmer():
    company = "Microsoft"
    def __init__(self, name, product):
         self.name = name
         self.product = product
    def getInfo(self):
        print(f"The name of the Company is {self.company} programmer is {self.name} and the progect is {self.product}")

zeon = Programmer("ZEON", "skype")
khalu = Programmer("Khalu", "Github")

zeon.getInfo()
khalu.getInfo()