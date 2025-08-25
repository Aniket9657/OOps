class TV :
    def F1(self):
       print(" Entertainment")




class Telephm:
    def F2(self):
        print("communication")



class Smartphn(TV,Telephm):
    def __init__(self):
        print("Smartphn is a child class")







S = Smartphn()
S.F1()
S.F2()


