class Student:
  def __init__(self,name,marks):
    self.name  = name
    self.marks = marks

  @staticmethod
  def welcom():
    print('Wellcome')

  def avg_mark(self):
    marksum = 0
    for val in self.marks:
      marksum += val
    avgMark = marksum/3
    print("Assalamu Alaikum ",self.name , "your avarage mark is:" , avgMark)


myclass = Student('Abdullah',[88,91,75])
myclass.welcom()
myclass.avg_mark()