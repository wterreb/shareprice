# Get stock price from https://www.google.co.nz/search?q=NZE:ERD

from bs4 import BeautifulSoup

import requests
import getopt

#url = input("Enter a website to extract the URL's from: ")
url = "https://www.google.co.nz"
defaultStockItem = "NZE:ERD"

import sys
def printf(format, *args):
    sys.stdout.write(format % args)

def scrapeSharePrice(stockcode ):
    r  = requests.get(url + "/search?q=" + stockcode)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    #content = soup.prettify(formatter="minimal")
    content = soup.prettify()
  #  print(content)
    all_items = soup.findAll('div', class_="g")
    one_item = str(all_items[0])
    oneline = one_item[one_item.index("http://www.google.com/finance")+one_item.index("?q="):]
    oneline = oneline[oneline.index("http://www.google.com/finance") + oneline.index("/finance/chart?"):]
    oneline = oneline[oneline.index("<b>")+3:]
    stockPrice = oneline[:oneline.index("</b>")]
    print(stockPrice)

def showhelp():
    print('usage : shareprice_google.py -s <sharecode>')
    print('example : python3 shareprice_google.py -s ' + defaultStockItem)

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