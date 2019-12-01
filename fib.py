#Author:Wilson

#fib noraml
#Time Complexity:TN= T(N-1)+T(N-2) O(2**N)

def fib(n):

    if n == 1 or n == 0:
        
        return 1
    else:
        
        return fib(n-1)+fib(n-2)

#for i in range(121):
#    print('fib(' + str(i) + ') =', fib(i))



#fib less space
#Time Complexity:O(n)
#Extra Space: O(1)

def fib_space(n):
    
    a = 0
    b = 1

    if n==0:
        
        return 0
    
    elif n==1:
        
        return 1
    
    else:
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 

#for i in range(121):
#   print('fib(' + str(i) + ') =', fibb(i))


# Memo style
#Time Complexity:O(n)

#fib search:

def fib_Memo(n,memo={}):

    if n == 0 or n == 1:
        memo[n]=1
        return 1
    else:
        if n-1 in memo and n-2 in memo:
            memo[n]= memo[n-1]+ memo[n-2]
            return memo[n]
        else:
           return fib_Memo(n-1)+fib_Memo(n-2)

for i in range(121):
    print('fib(' + str(i) + ') =', fib_Memo(i))


#fib search(by MIT6_0002F16_lec2 ):
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    
for i in range(121):
    print('fib(' + str(i) + ') =', fastFib(i))
