class Sum:
  def __init__(self):
    print("Default Constructor")
  def __init__(self,x,y):
    print("Parameterized Coonstructor")
    self.a=x
    self.b=y
  def add(self):
    self.c=self.a+self.b
  def show(self):
    print("The sum of",self.a,"and",self.b,"is",self.c)
  s1=Sum(8,1)
  s1.add()
  s1.show()
