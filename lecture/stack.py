# LIFO
card_stack = []

if __name__ == "__main__":
    card_stack.append('5 of diamonds')
    print(', '.join(card_stack))
    card_stack.append('3 of clubs')
    print(', '.join(card_stack))
    card_stack.append('ace of hearts')
    print(', '.join(card_stack))

    # pop from the top of the stack
    card_stack.pop()

    print(', '.join(card_stack))