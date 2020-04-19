def fibonacci_modified(t1, t2, n):
    array = [0] * n
    array[0] = t1
    array[1] = t2

    for i in range(2, n):
    	array[i] = array[i-2] + (array[i-1])**2
    return array[n-1]


if __name__ == '__main__':
    t1 = 0
    t2 = 1
    n = 5

    print('fib of', n, ':', fibonacci_modified(t1, t2, n))


