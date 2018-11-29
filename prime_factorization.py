import math

def trial_division(input):

    n = int(input)
    factorization = []

    #start w smallest possible prime factor
    min = int(2)
    while (n>1):
        if (n%min ==0):
            factorization.append(min)
            n= n/min
        else:
            min = min+1

    return factorization
