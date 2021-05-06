def fib(n):
    first = 1
    last = 1
    print(first)
    print(last)
    sum1 = 2
    print(sum1)
    while sum1 < n:
        if sum1 != 2:
            print(sum1)

        sum1 = first + last;

        first = last
        last = sum1


fib(200)
