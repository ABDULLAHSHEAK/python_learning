tasks = []
while True:
  todo = input('Enter Todo: ')
  list = {
    'title' : todo
  }
  tasks.append(list)
  adNew = input('Add New yes/no ')
  if(adNew == "no"):
    break

# print(tasks)
for task in tasks:
  print(task['title'])

