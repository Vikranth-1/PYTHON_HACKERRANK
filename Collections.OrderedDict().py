from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    d = OrderedDict()
    
    for _ in range(n):
        *name_parts, price = input().rsplit(' ', 1)
        item_name = ' '.join(name_parts)
        price = int(price)
        
        if item_name in d:
            d[item_name] += price
        else:
            d[item_name] = price
    
    for item, net_price in d.items():
        print(f"{item} {net_price}")
