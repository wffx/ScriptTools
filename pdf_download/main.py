from bs4 import BeautifulSoup
import html
from urllib import request,error
import sys
from urllib.parse import urljoin
import string
import wget


def main(argv):
    if len(argv) == 1:
        print("Need an url")
        return None

    url = argv[1]
    f = request.urlopen(url)
    res = f.read()

    html = BeautifulSoup(res, 'html.parser')
    #pat = re.compile(r'pdf')
    
    for tag in html.find_all("a"):       
        if tag['href'].find(".pdf") != -1 :
            st = tag["href"]
            if tag["href"][0] == '.':
                st = st[2:len(st)]
                st = url + st
            elif tag['href'].find("http") == -1:
                #and tag['href'].find("www") != -1:
                st = urljoin(url, st)
            print(st)    
            try:
                 wget.download(st)
            except error.HTTPError as e:
                print(e.code)
                pass
            
            continue

if __name__ == "__main__":
    main(sys.argv)
