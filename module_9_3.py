first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
third = zip(first, second)


first_result = ((len(a) % len(b)) for a, b in third if len(a) != len(b))
second_result = ((len(a) == len(b)) for a in first for b in second)

print(list(first_result))
print(list(second_result))

