#!/usr/bin/env python

"""
-------------------------------------------------------------------------------
Name:        hurricaneElectricLookup.py
Purpose:    Look up target network ranges using bgp.he.net
Author:        Justin Kennedy (@jstnkndy)
-------------------------------------------------------------------------------
"""

from bs4 import BeautifulSoup
import requests
import sys
import re
from netaddr import *

def usage():
    print "Usage: %s <search string>" % sys.argv[0]


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit()

    search = sys.argv[1]

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"}
    url = "http://bgp.he.net/search?search%5Bsearch%5D=" + search + "&commit=Search"
    browser = requests.get(url, headers=headers)

    soup = BeautifulSoup(browser.text)
    table = soup.find("table")
    
    try:
        rows = table.findAll("tr")
    except:
        print "No results found"
        sys.exit()

    #dictionary to store the cidrs
    cidrDict = dict()

    for row in rows:
        tds = row.findAll("td")
        try:
            cidr = str(tds[0].get_text())
            company = str(tds[1].get_text())

            #extract IPv4 CIDRs only
            if not re.match(ur'\d+\.\d+\.\d+\.\d+/\d{1,2}',cidr):
                continue
            
        except:
            continue
        
        cidrDict.setdefault(company,[]).append(cidr)

    for key in cidrDict:
        print key+":"

        #merge the CIDRs to remove any duplicates
        s1 = IPSet()
        for cidr in cidrDict[key]:
            s1.add(cidr)

        #print the resulting cidrs
        for cidr in s1.iter_cidrs():
            print cidr

        print ""
        

if __name__ == "__main__":
    main()
