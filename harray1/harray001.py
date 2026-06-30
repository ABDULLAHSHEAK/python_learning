# Write a program to add two number;
number1 = int(input('Enter Number 1 '))
number2 = int(input('Enter Number 2 '))

print(number1 + number2)

# Write a program to add two number with function ;

def addTwoNum(num1,num2):
  result = num1 + num2
  return result

number1 = int(input('Enter Number 1 '))
number2 = int(input('Enter Number 2 '))
finalResult = addTwoNum(number1,number2)
print(finalResult)
