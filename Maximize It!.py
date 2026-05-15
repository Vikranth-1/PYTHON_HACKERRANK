from itertools import product

if __name__ == "__main__":
    K, M = map(int, input().split())
    
    lists = []
    for _ in range(K):
        arr = list(map(int, input().split()))
        lists.append(arr[1:])  # First element is the length
    
    max_value = 0
    for combination in product(*lists):
        value = sum(x * x for x in combination) % M
        if value > max_value:
            max_value = value
    
    print(max_value)
