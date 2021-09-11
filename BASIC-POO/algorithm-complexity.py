#This is Basic algortihm complexity example from Platzi trainning courses

import time
import sys

def factorial(number):
    answer = 1

    while number > 1:
        answer *= number
        number -= 1

    return answer


def recursive_factorial(number):
    if number == 1:
        return 1
    else: 
        return number * factorial(number - 1)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    number = int(input('Enter the number to calculate it factorial: '))

    print('********************')
    print('Calculating factorial of ' + str(number))
    start = time.time()
    factorial(number)
    end = time.time()
    print('Execution duration: '+ str(end-start))

    print('')
    print('********************')
    print('Calculating recursive  factorial of ' + str(number))
    start = time.time()
    recursive_factorial(number)
    end = time.time()
    print('Execution duration: '+ str(end-start))

