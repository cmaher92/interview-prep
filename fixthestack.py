# stacked plates incorrectly
# first two items were always placed in the wrong order
# write a function that takes a stack as input and swaps the bottom two items
# mutate stack, don't return a new one
# push, pop, peak, size

stack = [2, 1, 3, 4, 5, 6, 7]

def fix_the_stack(stack):
    temp_stack = []
    second_to_last_element = None
    last_element = None
    while len(stack) > 2:
        temp_stack.append(stack.pop())

    if len(stack) == 2:
        second_to_last_element = stack.pop()
        last_element = stack.pop()
        stack.append(second_to_last_element)
        stack.append(last_element)
        while len(temp_stack) != 0:
            stack.append(temp_stack.pop())

    return stack

print fix_the_stack(stack)
