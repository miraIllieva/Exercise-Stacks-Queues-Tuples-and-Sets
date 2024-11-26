seta = set([int(num) for num in input().split()])
setb = set([int(num) for num in input().split()])

n = int(input())

for i in range(n):
    user_input = input().split()
    command = f'{user_input[0]} {user_input[1]}'
    numbers = [int(number) for number in user_input[2:]]

    if command == 'Add First':
        seta.update(numbers)
    elif command == 'Add Second':
        setb.update(numbers)
    elif command == 'Remove First':
        seta.difference_update(numbers)
    elif command == 'Remove Second':
        setb.difference_update(numbers)
    elif command == 'Check Subset':
        print(seta.issubset(setb) or setb.issubset(seta))

print(*sorted(seta), sep=', ')
print(*sorted(setb), sep=', ')
