class Sum:
  def __init__(self):
    print("Default Constructor")
    self.a=0
    self.b=0
    self.c=0
  def get(self):
    print("Enter two values:- ")
    self.a=int(input())
    self.b=int(input())
  def add(self):
    self.c=self.a+self.b
  def show(self):
    print("Sum of",self.a ,"and", self.b, "is",self.c)
s1=Sum()
s1.show()
s1.get()
s1.add()
s1.show()

