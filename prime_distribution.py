import math
import prettytable
import matplotlib.pyplot as plt


def prime_dist():

    print("Q1: See imported list of a million primes in primes1.txt.")

    primes = []
    primes = open("primes1.txt").read().split()
    # for i in primes:
    #    print(int(i))

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

    print("Q2: Percentage of first million primes ending in 1 is "+str(num1/10000)+"%, ending in 3 is "+str(num3/10000)+"%, ending in 7 is "+str(num7/10000)+"%, ending in 9 is "+str(num9/10000)+"%.")

    a = prettytable.PrettyTable(["Last Digit","Followed by Last Dig = 1", "Followed by Last Dig = 3", "Followed by Last Dig = 7", "Followed by Last Dig = 9"])
    # b = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 3:"])
    # c = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 7:"])
    # d = prettytable.PrettyTable(["Followed by Ending in:", "Ending in 9:"])

    #Question 3 and 4
    pos = int(0)
    curdig = int(0)
    nextdig = int(0)
    numtwins = int(0)
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
        #Q3
        if(curdig==1):
            if(nextdig==1):
                q3a1+=1
                # print(int(primes[pos]) , " ends in" , curdig, "Followed by ",int(primes[pos+1]) , " ends in " , nextdig)
            elif(nextdig==3):
                q3a3+=1
                # print(int(primes[pos]) , " ends in" , curdig, "Followed by ",int(primes[pos+1]) , " ends in " , nextdig)
            elif(nextdig==7):
                q3a7+=1
                # print(int(primes[pos]) , " ends in" , curdig, "Followed by ",int(primes[pos+1]) , " ends in " , nextdig)
            elif(nextdig==9):
                q3a9+=1
                # print(int(primes[pos]) , " ends in" , curdig, "Followed by ",int(primes[pos+1]) , " ends in " , nextdig)
        elif(curdig==3):
            if(nextdig==1):
                q3b1+=1
            elif(nextdig==3):
                q3b3+=1
            elif(nextdig==7):
                q3b7+=1
            elif(nextdig==9):
                q3b9+=1
        elif(curdig==7):
            if(nextdig==1):
                q3c1+=1
            elif(nextdig==3):
                q3c3+=1
            elif(nextdig==7):
                q3c7+=1
            elif(nextdig==9):
                q3c9+=1
        elif(curdig==9):
            if(nextdig==1):
                q3d1+=1
            elif(nextdig==3):
                q3d3+=1
            elif(nextdig==7):
                q3d7+=1
            elif(nextdig==9):
                q3d9+=1
        #Q4
        if( (int(primes[pos]) +2) == int(primes[pos+1])):
            numtwins +=1

        pos += 1

    a.add_row([1,q3a1,q3a3,q3a7,q3a9])
    a.add_row([3,q3b1,q3b3,q3b7,q3b9])
    a.add_row([7,q3c1,q3c3,q3c7,q3c9])
    a.add_row([9,q3d1,q3d3,q3d7,q3d9])
    print("\nQ3: \n",a)

    # a.add_row([1, q3a1])
    # a.add_row([3, q3a3])
    # a.add_row([7, q3a7])
    # a.add_row([9, q3a9])
    # print("\nQ3a: \n",a)
    # b.add_row([1, q3b1])
    # b.add_row([3, q3b3])
    # b.add_row([7, q3b7])
    # b.add_row([9, q3b9])
    # print("\nQ3b: \n",b)
    # c.add_row([1, q3c1])
    # c.add_row([3, q3c3])
    # c.add_row([7, q3c7])
    # c.add_row([9, q3c9])
    # print("\nQ3c: \n",c)
    # d.add_row([1, q3d1])
    # d.add_row([3, q3d3])
    # d.add_row([7, q3d7])
    # d.add_row([9, q3d9])
    # print("\nQ3d: \n",d)

    print("Q4: The number of twin primes is: ", numtwins)

    with open('primes_line.txt', 'w+') as f:
        for item in primes:
            f.write("%s\n" % item)

    #Graph for 5
    y_val = []
    less_primes = []
    iter = int(0)

    while (iter<30):
        less_primes.append(primes[iter])
        y_val.append(iter)
        iter+=1

    axes = int(less_primes[len(less_primes)-1])

    plt.plot(less_primes,y_val,'bo')
    plt.axis([0,iter,0,axes])
    plt.ylabel("π(x)")
    plt.xlabel("x")
    print("Q5: See table in popup. Limited number of values to show here because would otherwise not generate graph in reasonable amount of time. Click full screen button in upper right hand corner of popup to see in more detail.")
    plt.show()
