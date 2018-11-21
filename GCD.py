
def gcd_alg(x, y):

    #Modulus result determines if we have reached the GCD
    c = int(x) % int(y)

    #Base Case
    if c == 0:
        print(y)
        return y

    # Recursive Call
    else:
        return gcd_alg(y, c)




