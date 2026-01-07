# Password Generator
""" Develop a tool that generates random, strong passwords 
based on user-defined criteria (length, inclusion of numbers, symbols, etc.). 
This utilizes string manipulation and the random module. """

import random , string

symbols = ['@','!','&','%','#','*']
alphabet =  string.ascii_lowercase + string.ascii_uppercase + random.choice(symbols)
firstThreeCharc =  ''.join(random.choice(string.ascii_uppercase) for i in range(3))



def generatePassword(length):

    while True:
        randomPassWord = ''.join(random.choice(alphabet) for i in range(length))
        print('PW Lenght:' + str(len(randomPassWord)))
        print('IntialRandomPW:' + randomPassWord)
        randomPassWord = randomPassWord[3:]
    
        randomPassWordFinal  = firstThreeCharc + randomPassWord

        for char in symbols:
            if(char in randomPassWordFinal):
                return randomPassWordFinal
            else:
                print('symbol not found:'+ char)
                


myPassword = generatePassword(8)
print('Password:'+ myPassword)







