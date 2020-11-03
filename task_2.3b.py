def primes():
    value = 1
    while True:
        count = 0
        value = value + 1
        for val in range(value):
            try:
                if value % val == 0:
                    count = count + 1
                    if count > 1:
                        break
            except ZeroDivisionError:
                continue
        if count < 2:
            yield value


for i in range(10):
    print(primes())

