class Student:
  def __init__(self,studentName):
    self.name = studentName
    print('Student Info :')
  
info = Student('Abdullah')
print(info.name)