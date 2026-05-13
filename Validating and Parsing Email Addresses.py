import re
import email.utils

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        name, email_addr = email.utils.parseaddr(input())
        if re.match(r'^[a-zA-Z][a-zA-Z0-9\-\._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_addr):
            print(email.utils.formataddr((name, email_addr)))
