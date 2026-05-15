from itertools import combinations

if __name__ == "__main__":
    n = int(input())
    letters = input().split()
    k = int(input())
    
    indices = list(range(n))
    total_combinations = list(combinations(indices, k))
    
    count_with_a = 0
    for comb in total_combinations:
        if any(letters[i] == 'a' for i in comb):
            count_with_a += 1
    
    probability = count_with_a / len(total_combinations)
    print(f"{probability:.4f}")
