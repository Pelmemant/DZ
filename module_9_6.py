import itertools


def all_variants(text):
    for i in range(len(text)):
        for rezult_str in map(''.join, itertools.combinations_with_replacement(text, i+1)):
            if rezult_str in text:
                yield rezult_str


a = all_variants("abc")
for i in a:
        print(i)