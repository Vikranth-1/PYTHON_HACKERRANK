import re

s = input()
pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
