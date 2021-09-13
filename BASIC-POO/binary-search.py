"""Recursive interation for binary search
As a recomendation:
    * If your list is ordered - binary search without doubt
    * if your list is not ordered
        + if your search is going to be executed only once - preferred linear search
        * if you are going to execute more than one search, order the list and them use binary search
"""
import random


def binary_search(list, start, end, objective, count = 0):
    count = count + 1
    print('We are looking for ' + str(objective) + ' between ' + str(list[start]) + ' and ' + str(list[end-1]) 
        + ' - this is the iteration ' + str(count))

    if start > end or objective < list[start]:
        return False, count
    elif start == objective:
        return True, count
    
    middle_of_the_list = (start + end) // 2

    if list[middle_of_the_list] == objective:
        return True, count
    elif list[middle_of_the_list] < objective:
        return binary_search(list, middle_of_the_list + 1, end, objective, count = count)
    elif list[middle_of_the_list] > objective:
        return binary_search(list, start, middle_of_the_list - 1, objective, count = count)
    else:
        return False, count       


if __name__ == '__main__':
    list_size = int(input("Enter list size: "))
    objective = int(input("Enter the number you are looking for: "))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found, count = binary_search(list, 0, len(list), objective)

    print(list)
    print('Element ' + str(objective) + ' exist in the list'  if found else str(objective) + ' does not exist in the list' )   
    print('The solution was found in ' + str(count) + ' iterations')