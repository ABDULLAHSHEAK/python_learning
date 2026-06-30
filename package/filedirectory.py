import os
directoryPath = '/Photos/MAS/'
contents = os.listdir(directoryPath)

for item in contents:
  print(item)