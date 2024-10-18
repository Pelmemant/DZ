from pprint import pprint


def custom_write(file_name, strings):
    with open(file_name, 'w') as f:
        strings_positions = {}
        for i, s in enumerate(strings):
            position = f.tell()
            f.write(s + '\n')
            strings_positions[(i + 1, position)] = s

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
