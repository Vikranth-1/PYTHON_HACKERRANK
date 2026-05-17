from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    
    for _ in range(n):
        command = input().split()
        if command[0] == 'append':
            d.append(int(command[1]))
        elif command[0] == 'appendleft':
            d.appendleft(int(command[1]))
        elif command[0] == 'pop':
            d.pop()
        elif command[0] == 'popleft':
            d.popleft()
    
    print(' '.join(map(str, d)))
