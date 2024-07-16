def print_params(a, b, c):
    x = (a, b, c)
    return x

print_params(1, 'Строка', True)
print_params()
print_params(a, b)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1, 'Строка', True]
values_dict = {1: 1, 2: "Строка", 3: True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'Строка']
print_params(*values_list_2, 42)
