import random
import time as t
from os import system
print('length of password: ')
ln = int(input())
k = '1'
print('****MENU****\n1. add capital\n2. add small\n3. add special character\n4. add numbers\nif you wish to include more than one, type the consecutive number space seperated')
while ('1' in k) or ('2' in k) or ('3' in k) or ('4' in k):
    print("Enter your choice: ")
    k = input()
cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sml = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spl = ['!', ',', '#', '%', '&', '(', ')', '*', '+', ',',
       '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ]
nm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Generating your password, please wait...........")
v = "....."
for ct1 in range(10):
    system('cls')
    i = random.choice(nm)
    if i % 2 == 0:
        v = v+'.'
    else:
        v = v[:-1]
    print("Generating Password"+v)
    t.sleep(0.5)
system('cls')
pas = ''
while len(pas) < ln:
    if '1' in k:
        pas = pas+random.choice(cap)
        if len(pas) == ln:
            break
    if '2' in k:
        pas = pas+random.choice(sml)
        if len(pas) == ln:
            break
    if '4' in k:
        pas = pas+random.choice(num)
        if len(pas) == ln:
            break
    if '3' in k:
        pas = pas+random.choice(spl)
        if len(pas) == ln:
            break
print("Your password is\t"+pas)
