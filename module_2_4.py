numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
doble = []
primes = []
for i in numbers:
    if i > 1:
        for n in numbers:
            if i / n > 1 and i % n == 0 and n > 1:
                doble.append(i)
for i in numbers:
    if not (i in doble) and i > 1:
        primes.append(i)
not_primes = list(dict.fromkeys(doble))
print(primes)
print(not_primes)



