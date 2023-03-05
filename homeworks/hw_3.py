from random import randint
import datetime
from time import sleep

# Task 1
for y in range(1, 10):
    for x in range(1, 10):
        res = x * y
        print(res, end='\t')
    print()

# Task 2
age = True
while age:
    age = int(input('Enter your age: '))
    if age >= 18:
        print('Great! You can drive a car!')
    else:
        print('You cannot drive a car!')
    question = input('Repeat [Y/N]: ')
    if question.lower() == 'y':
        age = True
    elif question.lower() == 'n':
        print('Exit')
        age = False
    else:
        age = True

# Task 3
name = input('Enter your name: ')
print(f'Hello, {name}, try to guess number from 1 to 10')
number = randint(1, 10)
att = 0
start_time = 0
end_time = 0
while True:
    guess = (input('Enter your number: '))
    if guess.isdigit() is True:
        guess = int(guess)
        if guess > number:
            att += 1
            print('Less!')
        elif guess < number:
            att += 1
            print('More!')
        elif guess == number:
            att += 1
            print(f'{name}, you won with {att} attempt!')
            ask = input('Wanna play again? ')
            if ask != 'yes':
                print('Thanks for your game!')
                break
    else:
        print('Enter numbers, not strings!')

# Task 4
data = int(input("Укажите время для таймера (в минутах): "))
timer = str(datetime.timedelta(minutes=data))
h, m, s = timer.split(":")
h, m, s = int(h), int(m) - 1, int(s)

for hour in range(h, -1, -1):
    for minute in range(m, -1, -1):
        for second in range(59, -1, -1):
            print(f'\r{hour}:{minute}:{second}', end='', flush=True)
            sleep(1)
    else:
        m = 59

# Task 5
cnt = 0
proc = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if a + b + c == d + e + f:
                            cnt += 1
                            print(f'Lucky ticket #{cnt}: {a}{b}{c}{d}{e}{f}')
    proc = cnt / 999999 * 100
    proc_r = round(proc, 2)
    print(f'The amount of lucky tickets is: {cnt}')
    print(f'Percentage of lucky tickets is: {proc_r} %')

# Task 6
INDENT = ' '
STAR = '*'

rows = spaces = int(input("Высота ёлки: "))
stars = 1

for i in range(rows):
    print(f'{INDENT*spaces}{STAR*stars}{INDENT*spaces}')
    stars += 2
    spaces -= 1

# Task 7
summa = int(input('Введите сумму вклада: '))
years = int(input('Введите количество лет для вклада: '))
cnt = 0
for i in range(years):
    summa *= 1.1
    cnt += 1
    print(f'{cnt} год: {round(summa)} $')

# Task 8
n = int(input("Введите количество лесенок: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j,  end='')
    print()

# Task 9
end_number = int(input("Конечный номер Фибоначчи: "))
num1 = num2 = 0
while end_number > 0:
    result = num1 + num2
    num1, num2 = num2, result
    if num2 == 0:
        print(num2, end=' ')
        num2 += 1
    elif num2 > end_number:
        break

    print(num2, end=' ')
