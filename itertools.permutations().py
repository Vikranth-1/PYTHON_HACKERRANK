from itertools import permutations

if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    
    for perm in sorted(permutations(s, k)):
        print(''.join(perm))
