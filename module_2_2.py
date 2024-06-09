print('Введите три числа')
first = input()
second = input()
third = input()
if first == second == third:
    print(3)
elif first == second or first == third or third == second:
    print(2)
else:
    print(0)
