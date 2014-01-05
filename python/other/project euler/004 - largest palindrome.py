#problem 4 the largest palindrome product
palindrome = 0

def check(pal):                
        for i in range(100,1000): #all 3 digit numbers
                save = pal
                if (not (pal%i)) and (len(str(pal/i))==3):
                        return pal/i,i
                        break
        if save == pal:
                return 0
                
for n in range(10000,998002): #100*100 = 10000, 999*999 = 998001
        if n > 99999:
                half = (len(str(n))/2)
        else:
                half =(len(str(n))/2)-1
        half1 = str(n)[half:]
        half2 = (str(n)[:half])[::-1]
        if (half1 == half2) and check(n):
                palindrome = n
                
print palindrome, check(palindrome)
