def wrapper(f):
    def fun(l):
        formatted = []
        for num in l:
            if len(num) == 10:
                formatted.append("+91 " + num[:5] + " " + num[5:])
            elif len(num) == 11:
                formatted.append("+91 " + num[1:6] + " " + num[6:])
            elif len(num) == 12:
                formatted.append("+91 " + num[2:7] + " " + num[7:])
            elif len(num) == 13:
                formatted.append("+91 " + num[3:8] + " " + num[8:])
        f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
