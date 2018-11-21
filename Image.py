from PIL import Image
import random

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


this_list = sieve(100)




img = Image.new("RGB", (500, 500))
img.show() # see a black image
pixels = []

x = 0
counter = 0

while x < 500:
    y = 0
    while y < 500:

        value = math.sqrt(math.pow(x, 2) + math.pow(y,2)) #distance formula
        if this_list.count(value):
            color_one = random.randint(1, 256)
            color_two = random.randint(1, 256)
            color_three = random.randint(1, 256)
            #pixels.append((color_one, color_two, color_three))
            print("(",x,y,")")
            img.putpixel((x,y), (color_one, color_two, color_three) )

        else:
            img.putpixel((x, y), (255, 255, 255))
        y =  y + 1
        counter = counter + 1
    x = x +1
    counter = counter + 1

img.putdata(pixels)
img.show() # see a red image
