n, k = map(int, input().split())

def my_func(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return my_func(n - 1, k) + my_func(n - 1, k - 1)

print(my_func(n, k))