import random
import contextlib


first = 'Мама мыла раму'
second = 'Рамена мало было'

comparison_function = lambda x, y: x.startswith(y)

result = list(map(comparison_function, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with contextlib.redirect_stdout(open(file_name, 'a')) as f:
            for data in data_set:
                f.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


mystic_ball = MysticBall(['Да', 'Нет', 'Наверное'])
print(mystic_ball())