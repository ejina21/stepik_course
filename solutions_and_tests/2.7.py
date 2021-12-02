import itertools

def primes():
    lst = [2]
    yield 2
    ch = 2
    while True:
        ch += 1
        flag = 0
        for i in lst:
            if ch % i == 0:
                flag = 1
                break
        if not flag:
            lst.append(ch)
            yield ch

print(list(itertools.takewhile(lambda x : x <= 31, primes())))

