#This is Basic algortihm for graphic count example from Platzi trainning courses

def f(x):

    answer = 0 

    #loop will run 1000 times 
    for i in range(1000):
        answer +=1 

    #Loop depends on X
    for i in range(x):
        answer += 1

    #Execution is 2X^2
    for i in range(x):
        for j in range(x):
            answer += 1 
            answer += 1

    return answer 

    #The ammount of operations is 1002 (answer + 1st loop +  return) + x (2nd loop) + 2x^2 (3rd loop)

    