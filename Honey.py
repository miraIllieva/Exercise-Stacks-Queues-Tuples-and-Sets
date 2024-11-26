from collections import deque
bees = deque([int(num) for num in input().split()])
nectar = ([int(num) for num in input().split()])

operators = deque(input().split())
honey = 0

def calculate(bees, nectar, operator):
    if operator == '+':
        return abs(bees + nectar)
    elif operator == '-':
        return abs(bees - nectar)
    elif operator == '*':
        return abs(bees * nectar)
    elif operator == '/':
        if nectar == 0:
            return 0
        else:
            return abs(bees / nectar)

while bees and nectar:
    if nectar[-1] >= bees[0]:
        op = operators.popleft()
        bee = bees.popleft()
        n = nectar.pop()
        honey += calculate(bee, n, op)
    else:
        nectar.pop()
print(f'Total honey made: {honey}')

if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
