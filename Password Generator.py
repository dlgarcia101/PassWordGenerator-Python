# Password Generator
""" Develop a tool that generates random, strong passwords 
based on user-defined criteria (length, inclusion of numbers, symbols, etc.). 
This utilizes string manipulation and the random module. """

import random , string

symbols = ['@','!','&','%','#','*']
alphabet =  string.ascii_lowercase + string.ascii_uppercase + string.digits + random.choice(symbols)
firstThreeCharc =  ''.join(random.choice(string.ascii_uppercase) for i in range(3))




def generatePassword(length):

    randomPassWord = ''.join(random.choice(alphabet) for i in range(length))
    print('PW Lenght:' + str(len(randomPassWord)))
    print('randomPW:' + randomPassWord)
    randomPassWord = randomPassWord[3:]
    
    randomPassWord  = firstThreeCharc + randomPassWord


    return randomPassWord
    


myPassword = generatePassword(8)
print('Password:'+ myPassword)







