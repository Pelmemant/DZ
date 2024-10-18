def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    other_digits = str_number[1:] if len(str_number) > 1 else ''
    result = 1 if not other_digits else get_multiplied_digits(int(other_digits))
    return first * result


result = get_multiplied_digits(40302)
print(result)
