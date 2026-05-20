import re

if __name__ == '__main__':
    s = input()
    k = input()
    
    pattern = re.compile(f'(?=({k}))')
    matches = pattern.finditer(s)
    
    found = False
    for match in matches:
        found = True
        print((match.start(1), match.end(1) - 1))
    
    if not found:
        print((-1, -1))
