import time

factorial_memo = {}

def factorial(k):
    if k == 0:
        return 1 
    else:
        return k * factorial(k-1)
        
def factorial_with_memo(k):
    if k < 2: 
        return 1
     
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]
        
if __name__ == "__main__":
    start = time.time()
    print (factorial(4))
    print (factorial(5))
    cp = time.time()
    print ("----")
    print (factorial_with_memo(4))
    print (factorial_with_memo(5))
    end = time.time()
    print ("wo_memoization",cp-start)
    print ("with_memoization",end-cp)