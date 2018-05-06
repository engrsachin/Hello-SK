#!/usr/bin/python

import os
import time
import sys
import random


#now lets create this words for incoming
nameQ = ['what is your name', 'Whats your name', 'what is your name?', 'whats your name']
greetIn = ['hello', 'hi', 'hi there', 'hello there']
birth = ['what is your date of birth', 'what is your date of birth?', 'what is your DOB', 'what is your DOB?']
botmaster = ['who is your botmaster', 'who is your botmaster']

#will also need to create outgoing
greetOut = ['hi there', 'hello', 'hi my name is Sachin', 'hello there']
nameOut = ['I am called Sachin', 'My name is Sachin', 'I am called Sachin']

B = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
print(B)
while True:
    H = eval(input('=>').strip())
    HLower = H.lower()
    print (HLower)
    if H == '':
            print ('=> Thanks meeting your')
            time.sleep(1)
            os.system("sudo shutdown -h now")
            break
    elif HLower in nameQ:
            print ('=>' + (random.choice(nameOut)))
    elif HLower in greetIn:
        print ('=>' + (random.choice(greetOut)))
    elif HLower in botmaster:
        print('=> My botmaster is SK')
    elif HLower in birth:
        print('=> I was activated in the 25th of Feb 2017')
