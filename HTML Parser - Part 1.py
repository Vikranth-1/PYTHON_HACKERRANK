from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] else 'None'}")
    
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] else 'None'}")

if __name__ == "__main__":
    n = int(input())
    html_code = ""
    for _ in range(n):
        html_code += input()
    
    parser = MyHTMLParser()
    parser.feed(html_code)
