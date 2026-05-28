cube = lambda x: x ** 3  
def fibonacci(n):
    fib = [0, 1]
    [fib.append(fib[-2] + fib[-1]) for _ in range(n)]
    return fib[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
