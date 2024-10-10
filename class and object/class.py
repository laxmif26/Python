class Sum:
    def get(self):
        print("Enter 2 valus:- ")
        self.a=int(input())
        self.b=int(input())
    def add (self):
        self.c=self.a+self.b
    def show (self):
        print("sum of ",self.a ,"and", self.b,"is" ,self.c)
s1=Sum()
s1.get()
s1.add()
s1.show()
print(s1.c)
        
