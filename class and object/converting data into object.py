data=[("samir",1024,"indore",856321),("priya",1068,"pune",78178),("raaj",1089,"mumbai","57272")]
class Employee:
  def getData(self,name,id,city,salary):
    self.name=name
    self.id=id
    self.city=city
    self.salary=salary
  def showData(self):
    print("name\t: ",self.name)
    print("id\t: ",self.id)
    print("city\t: ",self.city)
    print("salary\t ",self.salary)
all_obj=[]
for x in data:
  e1=Employee()
  e1.getData(x[0],x[1],x[2],x[3])
  all_obj.append(e1)
i=1
for obj in all_obj:
  obj.showData()
  i+=1
