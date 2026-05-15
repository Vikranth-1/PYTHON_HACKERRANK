from itertools import combinations

if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    
    for i in range(1, k + 1):
        for comb in combinations(s, i):
            print(''.join(comb))
