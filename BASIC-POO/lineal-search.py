"""lineal search, look through elements in sequence 
"""
import random

def lineal_search(list, objective):
    match = False

    #Look depends on the input so this is O(n)
    for element in list:
        if element == objective:
            match = True
            break
            #this break will not change algorthm complexity if it found at the end

    return match

if __name__ == '__main__':
    list_size = int(input("Enter list size: "))
    objective = int(input("Enter the number you are looking for: "))

    list = [random.randint(0, 100) for i in range(list_size)]

    found = lineal_search(list, objective)

    print(list)
    print('Element ' + str(objective) + ' exist in the list'  if found else str(objective) + ' does not exist in the list' )    