# a function that calls on itself
def shortest():
    shortest()

# stackoverflow - all computer's memory allocated for
# the call stack is used up.

# limit = maximum recursion depth = maximum call stack size (1000 function calls)
if __name__ == "__main__":
    shortest()