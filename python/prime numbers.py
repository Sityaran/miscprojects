import math

def primed():
    divs = [2.0,3.0,5.0,7.0]
    primes = []
    
    for x in range(2,200):
        notprime = 0
        
        for y in range(0,4):
            check = x/divs[y]
            checked = int(math.ceil(check)) - check
            if checked == 0:
                if x != divs[y]:
                    notprime += 1
                    
        if notprime == 0:
            primes.append(x)
            
    print primes
    print len(primes)

def primed2():
    primes = []
    divs = []
    for i in range(2,7920):
        divs.append(i*1.0)
        
    for x in range(2,7920):
        notprime = 0
        for y in range(2,x):
            check = x/divs[y-2]
            check2 = math.ceil(check) - check
            if check2 == 0.0:
                if x != divs[y-2]:
                    notprime += 1
        if notprime == 0:
            primes.append(x)
    print primes
    print len(primes)

def primed3(a): #fastest method i had before i began project euler/learned about sieve
    maxcheck = a
    primes = []
    divs = []       
        
    for x in range(2,maxcheck+1):
        divs.append(x*1.0)
        notprime = 0
        for y in range(2,x):
            check = x/divs[y-2]
            check2 = math.ceil(check) - check
            if check2 == 0.0:
                if x != divs[y-2]:
                    notprime += 1
        if notprime == 0:
            primes.append(x)
    print primes
    print len(primes)

def sieve(a): #basic sieve algorithim
    maxprimes = a
    sieve = range(maxprimes)
    sieve[0],sieve[1] = False,False
    for i in range(2,maxprimes):
        if sieve[i]:
            for n in range((2*i),(maxprimes),i):
                sieve[n] = False
    for x in sieve:
        if x:
            print x,


def check():
    var1 = []
    var2 = []
    for i in range(0,1000):
        var1.append(i)
    for n in range(1,1000):
        var2.append(n)
    print len(var1)
    print len(var2)
    var1[999]
    var2[998]

sieve( int( raw_input("primes up to what value: ") ) )
raw_input("exit")
