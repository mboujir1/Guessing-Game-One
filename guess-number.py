#!/usr/bin/python3

import random

count = 0
MIN, MAX = 1, 9

while True:
    rand = random.randint(MIN, MAX)
    user_input = input('\nGuess a number between 1-9: ')
    
    if str(user_input).lower() == 'exit':
        break
        
    diff = abs(rand - int(user_input))
    count += 1

    if not int(user_input) in range(MIN,MAX+1):
        print('please choose number between 1-9')
        break
        
    elif (user_input == int(rand)):
        print('Amazing! you choosed the exact number.')
        
    elif diff < ((MAX+MIN)/2):
        print('your guess is too close!!!')
        
    else:
        print('your guess is too far away!!!')
        
    print('the number is ' + str(rand))
