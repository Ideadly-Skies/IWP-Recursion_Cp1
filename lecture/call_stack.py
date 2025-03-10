# program's call stack is a stack of frame object
# frame obj contain information about a single function call 

# frame obj are created and pushed onto the stack when function is called
# when the function return, that frame object is popped off the stack
def a():
    spam = 'Ant'
    print('spam is ' + spam)
    b()
    print('spam is ' + spam)

def b():
    spam = 'Bobcat'
    print('spam is ' + spam)
    c()
    print('spam is ' + spam)

def c():
    spam = 'Coyote'
    print('spam is ' + spam)

if __name__ == "__main__":
    a()