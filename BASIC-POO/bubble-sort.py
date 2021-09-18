"""This is an example using bubble sort algorith to order a random generated list"""

import random

def bubble_sort(list):
    len_list = len(list)

    for i in range(len_list):
        #This will avoid to go throught the list all over again, we remove the part previously ordered
        for j in range(0, len_list - i - 1): # O(n) * (n) [for inside a for] = O(n * n) = O(n ** 2)
            #this compares adjacents indexes and order the list
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        print(list)
    
    return list


if __name__ == '__main__':
    
    list_size = int(input('Enter the size of the list: '))

    list = [random.randint(0, 100) for i in range(list_size)]
    print('The list to order is: ' + str(list) + '\n')

    ordered_list = bubble_sort(list)
    print('\nThe final ordered list is: ' + str(ordered_list))