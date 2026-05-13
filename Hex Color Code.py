import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        line = input()
        matches = re.findall(r'(?<!^)(#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6})(?=;|\)|,|\s)', line)
        for match in matches:
            print(match)
