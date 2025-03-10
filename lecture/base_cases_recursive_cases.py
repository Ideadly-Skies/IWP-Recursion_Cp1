def shortestWithBaseCase(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.' % (makeRecursiveCall))
    if not makeRecursiveCall:
        # BASE CASE
        print('Returning from base case.')
        return 
    else:
        # RECURSIVE CASE
        shortestWithBaseCase(False)
        print('Returning from recursive case.')

if __name__ == "__main__":
    print('Calling shortestWithBaseCase(False):')
    shortestWithBaseCase(False) # returning from base case
    print()
    print('Calling shortestWithBaseCase(True):') # returning from recursive case
    shortestWithBaseCase(True)