from bs4 import BeautifulSoup

import requests
import getopt

#url = input("Enter a website to extract the URL's from: ")
url = "https://www.reuters.com/finance/stocks/chart/"
defaultStockItem = "ERD.NZ"

import sys
def printf(format, *args):
    sys.stdout.write(format % args)

def scrapeSharePrice(stockcode ):
    r  = requests.get(url + stockcode)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    all_items = soup.findAll('div', class_="sectionQuoteDetail")
    one_item = str(all_items[0])
    oneline = one_item[one_item.index("</span>"):]
    oneline = oneline[oneline.index("23px;") + 7:]
    oneline = oneline.strip()
    stockPrice = oneline[:oneline.index("</span>")]
    print(stockPrice)

def showhelp():
    print('usage : shareprice_reuters.py -s <sharecode>')
    print('example : python3 shareprice_reuters.py -s ' + defaultStockItem)

def main(argv):
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hs:", ["share="])
    except getopt.GetoptError:
        showhelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            showhelp()
            sys.exit()
        elif opt in ("-s", "--share"):
            scrapeSharePrice(arg)
            sys.exit()
    # Use default stock if not specified by caller
    scrapeSharePrice(defaultStockItem)

if __name__ == "__main__":
   main(sys.argv[1:])