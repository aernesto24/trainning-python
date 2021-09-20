"""
This is a merge-sort example
merge sort is an algorith that divides and conquer, divide list on equal parts until you get list of 1 or 0 elements
Algorithm nlogn
Merge Sort use recursion and iterations
Based on POO Training Platzi
"""

import random

def merge_sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left_list = list[:middle]
        right_list = list[middle:]
        print(left_list, '*' * 5, right_list)

        #Recursive call on each middle to divide each list on even smaller one (2 recursive call)
        merge_sort(left_list)
        merge_sort(right_list)

        #Iterators to walk through both lists
        i = 0
        j = 0
        
        #Iterator for main list
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1

            k += 1

        #while to copy what is left from left list
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        
        #while to copy what is left from right list
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

        print('left ' + str(left_list) + ' Right ' + str(right_list))
        print(list)
        print('-' * 50)

    return list


if __name__ == '__main__':
    list_size = int(input('Enter the size of the list: '))

    list = [random.randint(0, 100) for i in range(list_size)]
    print('The list to order is: ' + str(list) + '\n')
    print('-' * 20)

    ordered_list = merge_sort(list)
    print('\nThe final ordered list is: ' + str(ordered_list))