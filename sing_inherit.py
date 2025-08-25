class queen :
    def M1(self):
        print("Can move daigonally")



    def m2(self ):
        print("Can move Straight")



    def m3(self):
        print("can move any number of square")



class rook(queen):
    def R(self):
        print("rook is a child clas") 


class bishop(queen):
    def B(self):
        print("bishop is a child class") 



B = bishop()
R = rook()


B.M1()
R.m2()



