# Social Media GitHub,SnapChat,Twitter and etc..
# YazeedBnMohmmeD
# Biomedical Technlogist Bsc

# Massive Password Generator v1 


import random

print("Massive Password Generator v1 \n Github: YazeedBnMohmmeD \n \n")
    
ch = 'ZXCVBNM<>?":LKJHGFDSAQWERTYUIOP{}|+_)(*&^%$#@!~zxcvbnm,./;lkjhgfdsapoiuytrewq`1234567890'

nop = input('How many password do you want to generate?')
nop = int(nop)

lop = input('Whats the length of passwords?')
lop = int(lop)

for p in range (nop):
    password = ''
    for l in range(lop):
       password += random.choice(ch)
    print(password)
    pwd = open("passwords.txt", "a")
    pwd.write(password +"\n" )
    pwd.close()
