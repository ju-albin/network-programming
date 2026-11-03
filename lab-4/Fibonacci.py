def fibonacci(maxNumber):
    a,b = 1, 1
    while a < maxNumber:
        yield a
        a,b = b, a+b

def main(): 
    for i in fibonacci(100):
        print(i)

main()