number1 = float(input('Перше число: '))
number2 = float(input('Друге число: '))
action = input('Дія (+, -, *, /): ')

if action == '+':
    print(number1 + number2)
elif action == '-':
    print(number1 - number2)
elif action == '*':
    print(number1 * number2)
elif action == '/':
    if number2 == 0:
        print('Ділення на нуль заборонено !')
    else:
        print(number1 / number2)
else:
    print('Невідома дія !')