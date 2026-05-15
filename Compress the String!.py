from itertools import groupby

if __name__ == "__main__":
    s = input()
    
    result = []
    for key, group in groupby(s):
        result.append(f"({len(list(group))}, {key})")
    
    print(' '.join(result))
