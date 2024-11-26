seta = set([int(num) for num in input().split()])
setb = set([int (num) for num in input().split()])

n = int(nput())

for in range(n):
    user_input = input().split()
    command = f'{user_input[0]} {user_input[1]}'
    numbers = [int(number) for number in user_input[2:]]

    if command == 'Add First':
        seta.update(numbers)
    if command == 'Add Second':
        setb.update(numbers)
    if command == 'Remove First':
        sets.differance_update(numbers)
    if command = 'Remove Second':
        setb.differance_update(numbers)
    elif command = 'Check Subset':
        print(seta.issubset(setb) or setb.issubset(seta))
print(*sorted(seta), sep =', ')
print(*sorted(setb), sep = ', ')