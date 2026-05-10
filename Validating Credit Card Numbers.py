import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        card = input().strip()
        
        pattern = r'^[456]\d{3}(-?\d{4}){3}$'
        
        if re.match(pattern, card):
            no_hyphen = card.replace('-', '')
            if not re.search(r'(\d)\1{3,}', no_hyphen):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
