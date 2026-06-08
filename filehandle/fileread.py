# file = open('filehandle/test.txt','r')
# content = file.read()
# print(content)
# file.close()

with open('filehandle/test.txt','r') as f:
  print(f.read())