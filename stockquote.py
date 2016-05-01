# ****************************************
# This program finds the stock quote for the company
# Author : Deepak [SmushBall]
# Date : Dec 13, 2015
# *****************************************
import urllib, re, sys
symbol = sys.argv[1]
url = 'http://finance.google.com/finance?q='
content = urllib.urlopen(url+symbol).read()
m = re.search('span id="ref.*>(.*)<', content)
if m:
	quote = m.group(1)
else:
    quote = 'No quote for symbol: ' + symbol
print(quote)    	