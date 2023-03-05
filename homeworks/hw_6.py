# Task 1
dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}

dict1.update(dict2)
print(dict1)

# Task 2
n = int(input('Enter number: '))
dc = {i: i ** 2 for i in range(1, n + 1)}
print(dc)

# Task 3
num = [i for i in dc.values()]
cnt = len(num)
amount = sum(num)
aver_amount = amount / cnt
print(f'Total sum: {amount}')
print(f'Average number: {aver_amount}')

# Task 4
list1 = ['management', 'sales', 'hr', 'production', 'admins']
list2 = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50']
dc = {}
for i in range(len(list1)):
    dc[list1[i]] = list2[i]
print(dc)

# Task 5
cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}
moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']

num1 = round(((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5, 4)
num2 = round(((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5, 4)
num3 = round(((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5, 4)

distances['London-Paris'] = num1
distances['Moscow-London'] = num2
distances['Moscow-Paris'] = num3

print(distances)


# Task 1
a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

list_b = [i for i in a if i <= 5]
b = tuple(list_b)
list_c = [i for i in a if i > 5]
c = tuple(list_c)
print(b)
print(c)

# Task 2
name = input('Enter your name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))

a = [name, last_name, age]
b = tuple(a)
print(b)

# Task 3
numbers = input('Enter numbers separated by coma: ')
num = numbers.split(', ')
print(tuple(num))

# Task 4
names = input('Enter three names: ')
nms = names.split()
print(tuple(nms))

cnt = 0
for i in nms:
    cnt += 1
    print(f'Name {cnt}: ', i)

# Task 5
tuple_a = (1, 2, 3, 4, 5, 6, 7)
lst = [i ** 2 for i in tuple_a]
tuple_b = tuple(lst)
print(tuple_b)

# Task 6
numbers = (
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248,
    866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
    894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527
)

lst = [i for i in numbers[:numbers.index(815)] if i % 2 == 0]
print(lst)

# Task 7
numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
num = set(numbers)
lst = list(num)
tup = tuple(num)
print(lst)
print(tup)

# Task 8
config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'

lst_1 = list(config_sw1.split())[-1].split(',')
lst_2 = list(config_sw2.split())[-1].split(',')

sw1 = set(lst_1)
sw2 = set(lst_2)

print(sw1.intersection(sw2))
print(sw1.difference(sw2))
print(sw1.symmetric_difference(sw2))
print(sw1.union(sw2))


# Task 1
devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

n = input('Enter device [r1/r2/sw1]: ')
new_dc = {}
if n in devices.keys():
    new = dict(devices[n])
    val = list(new.values())
    new_dc['Расположен'] = val[0]
    new_dc['Вендор'] = val[1]
    new_dc['Модель'] = val[2]
    new_dc['Система (ios)'] = val[3]
    new_dc['IP адрес'] = val[4]
    for k, v in new_dc.items():
        print(k, v)
else:
    print('wrong type of device')

# Task 2
goods = {
 'Лампа': '12345',
 'Стол': '23456',
 'Диван': '34567',
 'Стул': '45678',
}

store = {
    '12345': [
     {'quantity': 27, 'price': 42}
    ],
    '23456': [
     {'quantity': 22, 'price': 510},
     {'quantity': 32, 'price': 520}
    ],
    '34567': [
     {'quantity': 2, 'price': 1200},
     {'quantity': 1, 'price': 1150}
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

goods['Лампа'] = store['12345']
goods['Стол'] = store['23456']
goods['Диван'] = store['34567']
goods['Стул'] = store['45678']

for key, value in goods.items():
    quantity = 0
    total_price = 0
    for i in value:
        quantity += i['quantity']
        total_price += i['quantity'] * i['price']
    print(f'Продукт: {key}, Количество: {quantity}, Стоимость: {total_price}')
