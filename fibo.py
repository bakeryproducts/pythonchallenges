# Sokolov 16/02/17
# Find sum of even numbers from Fibonacci series that contains N elements,
# and after this sum of digits in resulted number


def sum_fibo(n):
    a, b = 1, 1
    fibseq = []
    for _ in range(n):
        a, b = b, a + b
        if a % 2 == 0:
            fibseq.append(a)
    fibsum = sum(fibseq)
    print('Even numbers from Fibonacci series of {} elements: EvFi = {}'.format(n, fibseq))
    print('Total Sum(EvFi)= {}'.format(fibsum))
    res = sum([int(n) for n in str(fibsum)])
    return res


print('Sum of digits in total: {} '.format(sum_fibo(91)))