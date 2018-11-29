import math
import prettytable

primes = []
primes = open("primes1.txt").read().split()
#for i in primes:
#    print(primes)

num1 = int(0)
num3 = int(0)
num7 = int(0)
num9 = int(0)
right = int(0)

#Question 2
for i in primes:
    right = int(i)%10
    if(right==1):
        num1 += 1
    elif(right==3):
        num3 += 1
    elif(right==7):
        num7 += 1
    elif(right==9):
        num9 += 1

print("Percentage of first million primes ending in 1 is "+str(num1/1000000)+"%, ending in 3 is "+str(num3/1000000)+"%, ending in 7 is "+str(num7/1000000)+"%, ending in 9 is "+str(num9/1000000)+"%.")

a = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 1:"])
b = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 3:"])
c = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 7:"])
d = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 9:"])

#Question 3
pos = int(0)
current = int(0)
next = int(0)
curdig = int(0)
nextdig = int(0)
q3a1 = int(0)
q3a3 = int(0)
q3a7 = int(0)
q3a9 = int(0)
q3b1 = int(0)
q3b3 = int(0)
q3b7 = int(0)
q3b9 = int(0)
q3c1 = int(0)
q3c3 = int(0)
q3c7 = int(0)
q3c9 = int(0)
q3d1 = int(0)
q3d3 = int(0)
q3d7 = int(0)
q3d9 = int(0)
while(pos<(len(primes)-2)): #stops 1 before final item in list of primes
    curdig = int(primes[pos]) %10
    nextdig = int(primes[pos+1])%10
    #Q3a
    if(curdig==1):
        if(nextdig==1):
            q3a1+=1
        elif(nextdig==3):
            q3a3+=1
        elif(nextdig==7):
            q3a7+=7
        elif(nextdig==9):
            q3a9+=1
    elif(curdig==3):
        if(nextdig==1):
            q3b1+=1
        elif(nextdig==3):
            q3b3+=1
        elif(nextdig==7):
            q3b7+=7
        elif(nextdig==9):
            q3b9+=1
    elif(curdig==7):
        if(nextdig==1):
            q3c1+=1
        elif(nextdig==3):
            q3c3+=1
        elif(nextdig==7):
            q3c7+=7
        elif(nextdig==9):
            q3c9+=1
    elif(curdig==9):
        if(nextdig==1):
            q3d1+=1
        elif(nextdig==3):
            q3d3+=1
        elif(nextdig==7):
            q3d7+=7
        elif(nextdig==9):
            q3d9+=1
    pos += 1

a.add_row([1, q3a1])
a.add_row([3, q3a3])
a.add_row([7, q3a7])
a.add_row([9, q3a9])
print(a)
b.add_row([1, q3b1])
b.add_row([3, q3b3])
b.add_row([7, q3b7])
b.add_row([9, q3b9])
print(b)
c.add_row([1, q3c1])
c.add_row([3, q3c3])
c.add_row([7, q3c7])
c.add_row([9, q3c9])
print(c)
d.add_row([1, q3d1])
d.add_row([3, q3d3])
d.add_row([7, q3d7])
d.add_row([9, q3d9])
print(d)
