from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i + 1}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}.")


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')


def run_in_thread(word_count, file_name):
    t = Thread(target=write_words, args=(word_count, file_name))
    t.start()
    t.join()


run_in_thread(10, 'example5.txt')
run_in_thread(30, 'example6.txt')
run_in_thread(200, 'example7.txt')
run_in_thread(100, 'example8.txt')



