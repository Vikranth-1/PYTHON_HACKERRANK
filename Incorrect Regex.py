import re

n = int(raw_input())
for _ in range(n):
    s = raw_input()
    try:
        re.compile(s)
        print True
    except:
        print False
