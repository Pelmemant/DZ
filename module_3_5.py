def get_multiplied_digits(number):
    sum = 1
    last = number % 10
    if last == 0:
        last = 1
    number = number // 10
    if number != 0:
        sum = sum * get_multiplied_digits(number)
    return sum * last

result = get_multiplied_digits(40203)
print(result)