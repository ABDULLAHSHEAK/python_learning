dbusername = 'admin'
dbpass     = '123'
def checkLogin(username,passs):
  if(dbusername == username and dbpass == passs):
    print('login success')
  else:
    print('invalid user password')

inputuser = input('Enter your username ')
inputpass = input('Enter your pass ')
checkLogin(inputuser,inputpass)
