from bs4 import BeautifulSoup
import html
import urllib.request
import sys
import re
import string
import wget


def main(argv):
    if len(argv) == 1:
        print("Need an url")
        return None

    url = argv[1]
    f = urllib.request.urlopen(url)
    res = f.read()

    html = BeautifulSoup(res, 'html.parser')
    pat = re.compile(r'pdf')
    
    for tag in html.find_all("a"):       
        if tag['href'].find(".pdf") != -1 :
            st = tag["href"]
            if tag["href"][0] == '.':
                st = st[2:len(st)]
            st = url + st
            wget.download(st)
            print(st)

if __name__ == "__main__":
    main(sys.argv)
