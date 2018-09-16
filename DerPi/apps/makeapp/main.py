import sys, subprocess, os, easygui, urllib.request

idn = easygui.enterbox('Enter app id name')
#idn = 'test'
#icon = easygui.enterbox('Enter web image url (must be png)')
#icon = 'https://png.icons8.com/windows/1600/python.png'

try:
    os.mkdir('Apps\\' + idn)
    amain = open('Apps\\' + idn + '\\main.py', 'w')
    temp = open('app_template.txt', 'r')
    data = open('Apps\\' + idn + '\\data.txt', 'w')
    #urllib.request.urlretrieve(icon, 'Apps\\' + idn + '\\icon.png')
except:
    os.makedirs('..\\' + idn)
    amain = open('..\\' + idn + '\\main.py', 'w')
    temp = open('..\\..\\app_template.txt', 'r')
    data = open('..\\' + idn + '\\data.txt', 'w')
    #urllib.request.urlretrieve(icon, '..\\' + idn + '\\icon.png')

print(temp.read(), file=amain)
#amain.write(temp.read())
amain.close()
temp.close()
print(idn, file=data)
print('[]', file=data)
data.close()
