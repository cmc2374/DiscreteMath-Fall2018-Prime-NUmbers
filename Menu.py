#skeleton code taken from https://docs.python.org/2/library/tkinter.html#Tkinter.Tk (Python Software Foundation)
# This is GNU licenced and intended to be used as template as we have done below
import GCD
import Sieve
import Primality
import gen_image
from tkinter import *

class Application(Frame):
    def gcd(self):
        print("Enter Two Numbers")
        x = input()
        y = input()
        GCD.gcd_alg(x,y)

    def generate_primes(self):
        print("Generate Primes up to: ")
        x = input()
        print(Sieve.sieve(x))

    def primality_test_d(self):
        print("Enter A Number")
        x = input()
        Primality.divide_prime(x)

    def primality_test_s(self):
        print("Enter A Number")
        x = input()
        Primality.sieve_sift(x, Primality.sieve(x))

    def primality_test_f(self):
        print("Enter A Number")
        x = input()
        Primality.fermats_little(x)

    def generate_image(self):
         print("Enter A Number")
         x = input()
         gen_image.gen_image(x)

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
