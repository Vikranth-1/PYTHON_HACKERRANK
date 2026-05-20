import re

if __name__ == '__main__':
    n = int(input())
    
    for _ in range(n):
        line = input()
        
        # Replace && with and (only when surrounded by spaces)
        line = re.sub(r'(?<= )&&(?= )', 'and', line)
        
        # Replace || with or (only when surrounded by spaces)
        line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
        
        print(line)
