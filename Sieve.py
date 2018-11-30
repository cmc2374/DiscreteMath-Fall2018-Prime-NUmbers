

import math

def sieve(input):

    #local variables
    list= []
    final_list = []

    #Convert to integer
    n = int(input)

    #Fix indexing
    n = n + 1

    #Add all items to the list
    i = 0
    for x in range(0, n):
        list.append(i)
        i = i + 1

    #Sieve Algorithm to find primes
    ybank = []


    for y in range(2, int((math.sqrt(n))) + 1):
        y_test = 0
        #Speed buffs
        for z in ybank:
            if y % z == 0:
                y_test = 1
                break
        if y_test == 1:

            continue

        ybank.append(y)


        for x in range( y + y ,  n , y):
            if list[x] == 0:
                continue

            if y > x:
                print(x)
                break
            if x % y == 0:
                list.pop(x)
                list.insert(x,0)

   #Place all primes in a clean list

    list.pop(1)
    list.insert(1,0)
    for z in range(0, n ):
        if list[z] != 0:
            final_list.append(list[z])

    return final_list

