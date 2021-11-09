"""Example of list comprehension from platzi training
The goal is to store the square of the numbers from 1 to 100 that cannot be divided by 3

THe structure for comprehension is [element for element in interable if condition]"""

def run():

    #Remember that upper range is non-inclusive 
    not_div_nums = [i for i in range(1,101) if i % 3 != 0]
    print('The list of numbers not div by 3 are:')
    print(not_div_nums)

    print('*****************************************')
    print('The list of squares of previous numbers are:')
    squares_required = [i**2 for i in not_div_nums]
    print(squares_required)

    #You can do this on a single line by squares_required = [i**2 for i in not_div_nums if i % 3 != 0]
    #THe example above can be read as for each element in the iterable that comply with the condition, store the square of the element on a new list

    #Example of a list of elements that are mult of 4, 6, and 9 from 1 to 10000
    print('*****************************************')
    print('Print a list of element that are multiple of 4,6 and 9 from 1 to 10000')
    new_square_list = [i for i in range(1, 10001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(new_square_list)


if __name__ == '__main__':
    run()