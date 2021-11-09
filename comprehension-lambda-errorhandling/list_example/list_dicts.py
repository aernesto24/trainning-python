"""This is an example of dictionaries inside list and list inside dictionaries
From Platzi training
"""

def run():
    first_list = [1, "Hello", True, 4.5]
    first_dict = {"name": "Ernesto", "last_name": "Lopez"}

    #Now we are creating a list of dictionaries
    super_list = [
        {"name": "Ernesto", "last_name": "Lopez"},
        {"name": "DIna", "last_name": "Pent"},
        {"name": "Marc", "last_name": "Lopez"}
    ]

    #Now we are creating a group of lists INSIDE a dictionary
    super_dict = {
        "natural_nums" : [1, 2, 3, 4, 5],
        "integer_nums" : [-1, -2, 0, 1, 2],
        "floating_nums" : [1.1, 3,4, 5,6]
    }

    print('This is an example printing a dictionary with several list within')
    for key, value in super_dict.items():
        print('Key: ' + str(key).upper() + ' - ' + 'Value: ' + str(value))

    print('*****************************************************')
    print('\nThis is an example printing a list of dictionaries')
    for element in super_list:
        print(element)

    print('*****************************************************')
    print('\nThis is an example printing only the values of the dictionary inside the list')
    for element in super_list:
        print(list(element.values()))


if __name__ == '__main__':
    run()