# Task 1
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []
list3 = []
for i in list1:
    if i <= 5:
        list2.append(i)
    else:
        list3.append(i)
print(list2)
print(list3)

# Task 2
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your first age: '))

list_fio = (first_name, last_name, age)
print(list_fio)

# Task 3
nums = input('Enter numbers separated by commas with space: ')
list_num = nums.split(', ')
print(list_num)

# Task 4
addition = input('Enter an example with addition: ')
list_num = [int(i) for i in addition.split(' + ')]
res = sum(list_num)
print(f'Sum of numbers: {res}')

# Task 5
names = input('Enter three names separated by space: ')
list_name = names.split()
print(
    f'First name: {list_name[0]}'
    f'Second name: {list_name[1]}'
    f'Third name: {list_name[2]}'
)

# Task 6
numbers = [1, 2, 3, 4, 5, 6, 7]
sq_numbers = []
for i in numbers:
    i = i ** 2
    sq_numbers.append(i)
print(sq_numbers)

# Task 7
my_dishes = ['pizza', 'ice-cream', 'sushi', 'chocolate']
fr_dishes = my_dishes.copy()
fr_dishes[1] = 'french fries'
print(my_dishes)
print(fr_dishes)

# Task 8
num = int(input('Enter your number: '))
list_a = []
total = 0
for i in range(1, num + 1):
    list_a.append(i)
    total = sum(list_a)
print('Your list of numbers: ', list_a)
print('Sum of numbers: ', total)

# Task 9
list_even = [i for i in range(100) if i % 2 == 0]
list_odd = [i for i in range(100) if i % 2 == 1]
print(list_even)
print(list_odd)

# Task 10
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826,
    248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
    894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527
]

even_numbers = [i for i in numbers[:numbers.index(815)] if i % 2 == 0]
print(even_numbers)
lst = []
for num in numbers:
    if num == 815:
        break
    elif num % 2 == 0:
        lst.append(num)
print(lst)

# Task 11
list_num = list(input('Enter your number: '))
print('The number of simbols in your number: ', len(list_num))

# Task 12
start = int(input('Enter start number: '))
end = int(input('Enter finish number: '))
divider = 0
for number in range(start, end + 1):
    for any_number in range(2, number):
        if number % any_number == 0:
            divider = divider + 1
    if divider == 0 and number > 1:
        print(number)
    else:
        divider = 0

# Task 13
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
lst = ['Protocol', 'Network', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound interface']
ospf = ospf_route.split(', ')
ospf1 = ospf[0].split()
ospf2 = ospf[1::]
ospf3 = ospf1[1::]
ospf3.remove('via')
ospf3.extend(ospf2)
ospf3.insert(0, 'OSPF')
dc = dict(zip(lst, ospf3))
for k, v in dc.items():
    print(k, v)

# Task 14
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlan = config.split()[-1].split(',')
print(vlan)
