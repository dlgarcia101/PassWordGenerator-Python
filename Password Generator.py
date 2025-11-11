# Password Generator
""" Develop a tool that generates random, strong passwords 
based on user-defined criteria (length, inclusion of numbers, symbols, etc.). 
This utilizes string manipulation and the random module. """

import random , string

symbols = ['@','!','&','%','#']
alphabet =  string.ascii_lowercase + string.ascii_uppercase + string.digits + random.choice(symbols)

passwordLenght = 12


def generatePassword(length):
    randomPassWord = ''.join(random.choice(alphabet)for i in range(length))
    return randomPassWord



myPassword = generatePassword(12)
print('Password:'+ myPassword)







