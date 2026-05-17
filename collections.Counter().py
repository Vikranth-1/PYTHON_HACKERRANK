from collections import Counter

if __name__ == '__main__':
    n = int(input())
    shoes = Counter(map(int, input().split()))
    customers = int(input())
    
    total = 0
    for _ in range(customers):
        size, price = map(int, input().split())
        if shoes[size] > 0:
            total += price
            shoes[size] -= 1
    
    print(total)
