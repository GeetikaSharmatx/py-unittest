def add(x, y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y==0:
        raise ValueError('Cannot divide by zero')
    return x/y

def multiples():
    sum = 0
    for i in range(20):
        if i%5==0 or i%7==0:
            sum += i
    return sum
