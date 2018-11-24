import math
def divide_prime(input):

    #convert to int
    n = int(input)

    #Floor function of sqrt() is our max
    max = int(math.floor((math.sqrt(n))))

    #Divide n by i in the range of 2->sqrt(n)
    for i in range(2, max + 1):

        if n % i == 0:
            print(n, " is NOT prime")
            return 0

    print(n, "is prime")
    return 1


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

def sieve_sift(num, list):

    #number we want to find
    n = int(num)

    #len of list

    l = len(list)

    #final element
    final = list[l - 1]


    # count finds number instances of an item in a list
    if list.count(n) == 0:
        print(n, " is NOT prime")

    else:
        print(n, "is prime")


def fermats_little(input):

    # convert to int
    n = int(input)

    value = int(math.pow(2, n))
    if value % n == 2 % n:
        print(n, " is prime")

    else:

        print(n, " is NOT prime")