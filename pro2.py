class Books:
    def __init__ (self,type,title):

        self.type = type
        self.title= title 


    def Show(self):
        print("type: "+self.type)
        print("title: "+self.title)


B = Books("Novel ","Metamorphosis")  
B.Show()        