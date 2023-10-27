def SieveOfEratosthenes(n, isPrime):
  
    isPrime[0] = isPrime[1] = False
    for i in range(2,n+1):
        isPrime[i] = True
  
    for p in range(2,n+1):
        
        if (p*p<=n and isPrime[p] == True):
            # Update all multiples of p
            for i in range(p*2,n+1,p):
                isPrime[i] = False
                p += 1
def superPrimes(n):
     
    isPrime = [1 for i in range(n+1)]
    SieveOfEratosthenes(n, isPrime)
  
    # Storing all the primes generated in a
    # an array primes[]
    primes = [0 for i in range(2,n+1)]
    j = 0
    for p in range(2,n+1):
       if (isPrime[p]):
           primes[j] = p
           j += 1
  
    # Printing all those prime numbers that
    # occupy prime numbered position in
    # sequence of prime numbers.
    for k in range(j):
        if (isPrime[k+1]):
            print (primes[k],end=" ")
 
n = 241
print ("\nSuper-Primes less than or equal to ", n, " are :",)
superPrimes(n)
