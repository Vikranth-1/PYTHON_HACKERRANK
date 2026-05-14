from collections import deque

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = deque(map(int, input().split()))
        
        top = float('inf')
        possible = True
        
        while cubes:
            if cubes[0] >= cubes[-1]:
                current = cubes.popleft()
            else:
                current = cubes.pop()
            
            if current <= top:
                top = current
            else:
                possible = False
                break
        
        print("Yes" if possible else "No")
