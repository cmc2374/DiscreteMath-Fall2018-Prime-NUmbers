import math
import time
import prettytable

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
    time1 = trial_division(8)
    time1 = elapsed_time = time.time() - start_time
    time2 = trial_division(82)
    time2 = elapsed_time = time.time() - start_time
    time3 = trial_division(852)
    time3 = elapsed_time = time.time() - start_time
    time4 = trial_division(4852)
    time4 = elapsed_time = time.time() - start_time
    time5 = trial_division(77852)
    time5 = elapsed_time = time.time() - start_time
    time6 = trial_division(345852)
    time6 = elapsed_time = time.time() - start_time
    time7 = trial_division(8509342)
    time7 = elapsed_time = time.time() - start_time
    time8 = trial_division(84928352)
    time8 = elapsed_time = time.time() - start_time
    time9 = trial_division(843847352)
    time9 = elapsed_time = time.time() - start_time
    # time10 = trial_division(8348576952)
    # time10 = elapsed_time = time.time() - start_time
    # time11 = trial_division(85394857202)
    # time11 = elapsed_time = time.time() - start_time
    # time12 = trial_division(848475930452)
    # time12 = elapsed_time = time.time() - start_time
    # time13 = trial_division(8548574637292)
    # time13 = elapsed_time = time.time() - start_time
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
    # a.add_row([1, time10])
    # a.add_row([1, time11])
    # a.add_row([1, time12])
    # a.add_row([1, time13])
    print("Q3 Table: \n",a,"\nEnter number below to prime factorize it.")
