''' This is asymptotic notation or BIG O notation Example from platzi '''

#Sum law

def sum_law(n):
    # 0(n) + O(n) = O(n+n) = O(2n) = O(n) 

    for i in range(n):
        print(i)

    for i in range(n):
        print(i)


def sum_law_w_exp(n):
    #O(n) + O(n * n) = O(n + n^2) = O(n^2)  growth on this

    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)


def mult_law(n):
    #O(n) * O(n) = O(n * n) = O(n^2)

    for i in range(n):
        for j in range(n):
            print(i,j)


def fibonacci(n):
    #Recursive
    #O(2**n)
    if n == 0 and n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)