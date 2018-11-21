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
    i = 0;
    for x in range(0, n):
        list.append(i)
        i = i + 1

    #Sieve Algorithm to find primes
    for y in range(2, int(math.sqrt(n))):
        for x in range( y + 1, n):
            if x % y == 0:
                list.pop(x)
                list.insert(x,0)

   #Place all primes in a clean list
    for z in range(0, n):
        if list[z] != 0:
            final_list.append(list[z])

    return final_list


def table(list):

    #Len of primes
    x = len(list)

    #Scale for our table
    scale = int(x/10)

    for i in range(0, x):

        if i % scale == 0:
            print('\n')
            print("Scale: ", i + 1, "->", i +scale)

        print(list[i], end=" ")


