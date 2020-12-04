i = 0

while i < 101:
    out = i

    if i % 3 == 0 and i != 0:
        out = 'Fizz'

    if i % 5 == 0 and i != 0:
        if out == i:
            out = 'Buzz'
        else:
            out = 'FizzBuzz'

    print(out)
    i = i + 1
