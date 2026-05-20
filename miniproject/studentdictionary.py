students = []

while True:
  name = input('Enter your name ')
  roll = int(input('Enter your roll '))

  student = {
    "name" : name,
    "roll" : roll
  }
  students.append(student)

  more = input("Add more ? yes/no ")
  if(more == 'no'):
    break


# print(students)
# for key,value in students.items():
#   print(key,value)

for student in students:
   print(f"Name: {student['name']}, Roll: {student['roll']}")