import re

def is_valid_uid(uid):
    # Rule 5: Must have exactly 10 characters
    if len(uid) != 10:
        return False
    
    # Rule 3: Only alphanumeric characters
    if not uid.isalnum():
        return False
    
    # Rule 4: No character should repeat
    if len(set(uid)) != len(uid):
        return False
    
    # Rule 1: At least 2 uppercase letters
    uppercase_count = sum(1 for char in uid if char.isupper())
    if uppercase_count < 2:
        return False
    
    # Rule 2: At least 3 digits
    digit_count = sum(1 for char in uid if char.isdigit())
    if digit_count < 3:
        return False
    
    return True

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        uid = input().strip()
        if is_valid_uid(uid):
            print("Valid")
        else:
            print("Invalid")
