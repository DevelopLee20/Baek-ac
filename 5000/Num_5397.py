def push(stack:list, key:str):
    stack.append(key)

def pop(stack:list):
    if len(stack):
        return stack.pop()

for _ in range(int(input())):
    enter = [input()]
    stack_one = []; stack_two = []

    for key in enter:
        if key == '-':
            pop(stack_one)
        elif key == '<':
            key = pop(stack_one)
            print("test", key)
            if key is not None:
                push(stack_two, key)

        elif key == '>':
            key = pop(stack_two)
            if key is not None:
                push(stack_one, key)
        else:
            push(stack_one, key)

    output = ''
    for i in (stack_one+stack_two):
        output += i
    print(output)
