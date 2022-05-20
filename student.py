class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
     self.name = name
     self.age = age
     self.gender = gender
     self.level = level
     self.grades = grades

    def Start(self):
       print("This is my age")

John = Student("John","16","Male",10,4.5)   

print(John.Start())