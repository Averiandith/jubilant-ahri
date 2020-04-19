# https://www.hackerrank.com/challenges/html-parser-part-1/problem
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr, attr_val in attrs:
            print(f"-> {attr} > {attr_val}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr, attr_val in attrs:
            print(f"-> {attr} > {attr_val}")

# Input
n = int(input())
lines = [input() for _ in range(n)]

# Parsing
parser = MyHTMLParser()
for line in lines:
    parser.feed(line)
