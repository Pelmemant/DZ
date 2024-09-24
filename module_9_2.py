first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
third_strings = first_strings + second_strings

first_result = [len(first) for first in first_strings]
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]
third_result = {first: len(first) for first in third_strings if len(first) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)

