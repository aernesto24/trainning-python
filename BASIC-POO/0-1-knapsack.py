"""This is an example of how to solve the 0-1 knapsack problem
    Also some sorting will be added to grab the items ordered by weight"""

def backpack(size_backpack, weights, values, n):
    #print(size_backpack, weights, values, n)

    #The following if is our base case, no more values or the backpack is full
    if n == 0 or size_backpack == 0:
        return 0

    #Other base case is that the element i want to include in the backpack is bigger than the backpack
    if weights[n - 1] > size_backpack:
        return backpack(size_backpack, weights, values, n-1)

    #masx function return the max values between 2 possible values
    #First part inside max() is what happen if i select the item, the second part is what happen if i do not select the item
    return max(values[n-1] + backpack(size_backpack - weights[n-1], weights, values, n-1), 
        backpack(size_backpack, weights, values, n-1))


def sort_lists(weights, values):
    #Merge the 2 lists into one
    zipped_pairs = dict(zip(weights, values))
    
    #obtaining the key(weights) of the zipped list
    zipped_pairs_items = zipped_pairs.items()

    #sort based on the keys (weights)
    sorted_zipped_pair = sorted(zipped_pairs_items)
     
    return sorted_zipped_pair


if __name__ == '__main__':

    n_values = int(input('Enter the number of elements on the value list: '))
    values = list(map(int,input('\nEnter the values, separate by a whitspace: ').strip().split()))[:n_values]
    
    print('\n\n*************\n\n')

    n_weights = int(input('Enter the number of elements on the weights list: '))
    
    if n_weights == n_values:
        weights = list(map(int,input('\nEnter the weight values (Kg), separate by a whitspace: ').strip().split()))[:n_weights]
    else:
        print('The amout of values must be the same as the amount of weights')

    #For this example i am going to treat the size backpack as a constant
    size_backpack = int(input('\nEnter the initial value for size of the backpack(Kg): '))

    n = len(values)

    #This will sort the weights so they can be grabbed in order
    sort_list_result = sort_lists(weights, values)
    print('\nOrdering the Values' + str(sort_list_result))

    #This will separate again the weights and values on 2 lists but ordered 
    sort_list_result = dict(sort_list_result)
    weights, values = zip(*sort_list_result.items())

    #Execution ...
    result = backpack(size_backpack, weights, values, n)
    print('\nThe maximum value that you can grab is: ' + str(result))