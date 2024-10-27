import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline().strip()
        while line != '':
            all_data.append(line)
            line = file.readline().strip()
    return all_data


def linear_read_files(file_names):
    start_time = time.perf_counter()
    results = []
    for filename in file_names:
        result = read_info(filename)
        results.extend(result)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Линейное выполнение заняло {total_time:.4f} секунд.")
    return results


def multi_process_read_files(file_names):
    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, file_names)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Многопроцессное выполнение заняло {total_time:.4f} секунд.")
    return results


if __name__ == "__main__":
    file_names = [f'./file {number}.txt' for number in range(1, 4)]
    results_linear = linear_read_files(file_names)
    results_multi = multiprocessing.Process(target=multi_process_read_files, args=(file_names, ))
    results_multi.start()