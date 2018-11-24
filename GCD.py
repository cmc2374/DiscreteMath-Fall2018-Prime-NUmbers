
def gcd_alg(x, y):

    #Modulus result determines if we have reached the GCD
    c = int(x) % int(y)

    #Base Case
    if c == 0:
        print("answer: ", y)
        return y

    # Recursive Call
    else:
        print("gcd(", y, c, ")")
        return gcd_alg(y, c)




