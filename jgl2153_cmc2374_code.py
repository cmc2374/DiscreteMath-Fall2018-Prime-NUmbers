import PIL.Image
from tkinter import *
#skeleton code taken from https://docs.python.org/2/library/tkinter.html#Tkinter.Tk (Python Software Foundation)
# This is GNU licenced and intended to be used as template as we have done below

import random
import math
import time
import prettytable
import matplotlib.pyplot as plt

#GCD
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

#Sieve
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

#Primality
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

#gen_image

def gen_image(input):

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


    this_list = final_list
    #format the image
    size = n
    img = PIL.Image.new("RGB", (size, size))
    pixels = []

    x = 0
    counter = 0

    while x < size:
        y = 0
        while y < size:

            value = math.sqrt(math.pow(x, 2) + math.pow(y,2)) #distance formula

            #plot by distance from the origin if the distance is prime
            if this_list.count(value):
                color_one = random.randint(1, 255)
                color_two = random.randint(1, 255)
                color_three = random.randint(1, 255)
                #pixels.append((color_one, color_two, color_three))
                img.putpixel((x,y), (color_one, color_two, color_three) )

            else:
                #put a white pixel where no color there is not a prime distance
                img.putpixel((x, y), (255, 255, 255))
            y =  y + 1
            counter = counter + 1
        x = x +1
        counter = counter + 1

    #fill in data
    img.putdata(pixels)

    #align to standard cartesian coordinates
    img.rotate(90).show()


#prime_factorization
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

def time_check():
    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(1,10))
    elapsed_time = time.time() - start_time
    time1 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(10,100))
    elapsed_time = time.time() - start_time
    time2 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(100,1000))
    elapsed_time = time.time() - start_time
    time3 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(1000,10000))
    elapsed_time = time.time() - start_time
    time4 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(10000,100000))
    elapsed_time = time.time() - start_time
    time5 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(100000,1000000))
    elapsed_time = time.time() - start_time
    time6 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(1000000,10000000))
    elapsed_time = time.time() - start_time
    time7 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(10000000,100000000))
    elapsed_time = time.time() - start_time
    time8 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(100000000,1000000000))
    elapsed_time = time.time() - start_time
    time9 = elapsed_time/10

    start_time = time.time()
    for i in range(1,10):
        trial_division(random.randint(1000000000,10000000000))
    elapsed_time = time.time() - start_time
    time10 = elapsed_time/10
    #
    # start_time = time.time()
    # for i in range(1,10):
    #     trial_division(random.randint(10000000000,100000000000))
    # elapsed_time = time.time() - start_time
    # time11 = elapsed_time/10

    # for i in range(1,100):
    #     trial_division(random.randint(100000000000,1000000000000))
    # time12 = time.time() - time11
    # for i in range(1,100):
    #     trial_division(random.randint(1000000000000,10000000000000))
    # time13 = elapsed_time = time.time() - time12
    a = prettytable.PrettyTable(["Number of Digits:", "Time (Seconds):"])
    a.add_row([1, time1])
    a.add_row([2, time2])
    a.add_row([3, time3])
    a.add_row([4, time4])
    a.add_row([5, time5])
    a.add_row([6, time6])
    a.add_row([7, time7])
    a.add_row([8, time8])
    a.add_row([9, time9])
    a.add_row([10, time10])
    # a.add_row([11, time11])
    # a.add_row([12, time12])
    # a.add_row([13, time13])
    print("Q3 Table: \n",a,"\nEnter number below to prime factorize it.")

#prime_distribution
def prime_distr():

    print("Q1: See imported list of a million primes in primes1.txt. Contains prime numbers up to 15485863.")

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


#Menu
class Application(Frame):
    def gcd(self):
        print("Enter Two Numbers")
        x = input()
        y = input()
        gcd_alg(x,y)

    def generate_primes(self):
        print("Generate Primes up to: ")
        x = input()
        print(sieve(x))

    def primality_test_d(self):
        print("Enter A Number")
        x = input()
        divide_prime(x)

    def primality_test_s(self):
        print("Enter A Number")
        x = input()
        sieve_sift(x, sieve(x))

    def primality_test_f(self):
        print("Enter A Number")
        x = input()
        fermats_little(x)

    def generate_image(self):
        print("Enter A Number")
        x = input()
        gen_image(x)

    def prime_fact(self):
        print("Might take a minute or two to finish Q3 time check. If you would like to check for more digits, simply go to code and uncomment sections that iterate more digits (shortened here so user doesn't have to wait so long)")
        time_check()
        print("Enter A Number")
        x = input()
        print(trial_division(x))

    def prime_dist(self):
         prime_distr()

    def createWidgets(self):

        #QUIT BUTTON
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "right"})

        #GCD BUTTON
        self.gcd_button = Button(self)
        self.gcd_button["text"] = "GCD",
        self.gcd_button["command"] = self.gcd
        self.gcd_button.pack({"side": "left"})

        #PRIME NUMBER GENERATOR BUTTON
        self.gen_prime = Button(self)
        self.gen_prime["text"] = "Generate Primes"
        self.gen_prime["command"] = self.generate_primes
        self.gen_prime.pack({"side": "left"})

        #PRIMALITY DIVISION TEST BUTTON
        self.prime_test_d = Button(self)
        self.prime_test_d["text"] = "Primality Division Test"
        self.prime_test_d["command"] = self.primality_test_d
        self.prime_test_d.pack({"side": "left"})

        # PRIMALITY SIEVE TEST BUTTON
        self.prime_test_s = Button(self)
        self.prime_test_s["text"] = "Primality Sieve Test"
        self.prime_test_s["command"] = self.primality_test_s
        self.prime_test_s.pack({"side": "left"})

        # PRIMALITY FERMATS LITTLE THEOREM BUTTON
        self.prime_test_f = Button(self)
        self.prime_test_f["text"] = "Primality Test Fermat's Little Theorem"
        self.prime_test_f["command"] = self.primality_test_f
        self.prime_test_f.pack({"side": "left"})

        # GENERATE PRIME FACTORIZATION BUTTON
        self.prime_factorization = Button(self)
        self.prime_factorization["text"] = "Prime Factorization"
        self.prime_factorization["command"] = self.prime_fact
        self.prime_factorization.pack({"side": "left"})

        # GENERATE PRIME DISTRIBUTION BUTTON
        self.prime_distribution = Button(self)
        self.prime_distribution["text"] = "Prime Distribution"
        self.prime_distribution["command"] = self.prime_dist
        self.prime_distribution.pack({"side": "left"})

        # GENERATE IMAGE BUTTON
        self.gen_img = Button(self)
        self.gen_img["text"] = "Generate Image"
        self.gen_img["command"] = self.generate_image
        self.gen_img.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
