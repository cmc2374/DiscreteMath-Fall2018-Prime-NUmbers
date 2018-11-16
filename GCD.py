print("Hello World ")
print("Enter Two Numbers: ")

x = input()
y = input()



def GCD(p, q):

    c = p % q
    if (c == 0):
        return q
    else:
        return GCD(q, c)


print(GCD(int(x),int(y)))
