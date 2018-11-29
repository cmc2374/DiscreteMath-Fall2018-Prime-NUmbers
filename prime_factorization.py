  import math

  def trial_division(input):

      n = int(input)
      factorization = []

      #start w smallest possible prime factor
      minf = 2
      while n>1:
          if n%f ==0:
              factorization.append(f)
              n= n/f
          else:
              f = f+1

      return factorization
