def a():
    print('a() was called')
    b()
    print('a() is returning') 

def b():
    print('b() was called')
    c()
    print('b() is returning')

def c():
    print('c() was called')
    print('c() is returning')

if __name__ == "__main__":
    # output is given in reverse order.
    # each time a function returns, it remembers which line of code originally called it. 
    a() 