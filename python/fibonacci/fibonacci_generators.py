def fibonacci(limit):
    a,b = 0,1
    while b<=limit:
        yield b
        a,b = b,b+a
    
if __name__ == "__main__":
    try:
        limit =int(input("Enter the limit upto which Fibonacci series should be generated"))
        iter = fibonacci(limit)
        cnt = 0
        for i in iter:
            cnt +=1
            print (cnt,i)
    except KeyboardInterrupt:
        print ("Keyboard Interrupt. Quitting")
    except Exception as e:
        print ("Error: ",e)
        
