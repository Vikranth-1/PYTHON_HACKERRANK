from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

if __name__ == "__main__":
    n = int(input())
    html_code = ""
    for _ in range(n):
        html_code += input() + "\n"
    
    parser = MyHTMLParser()
    parser.feed(html_code)
