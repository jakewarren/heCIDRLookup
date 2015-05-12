# heCIDRLookup
Return CIDRs from bgp.he.net for a search string. The results are sorted by company and the CIDRs are merged to remove duplicate entries.

Based on the script from Justin Kennedy (@jstnkndy)

######Requirements:
```
netaddr
BeautifulSoup
requests
```

######Usage:
```
./hurricaneElectricLookup.py Facebook
Facebook:
31.13.64.0/23
31.13.66.0/24
31.13.68.0/22
31.13.72.0/21
31.13.80.0/21
31.13.90.0/23
31.13.93.0/24
31.13.95.0/24

Facebook, Inc.:
66.220.144.0/20
69.63.176.0/20
69.171.224.0/19
74.119.76.0/22
173.252.64.0/18
204.15.20.0/22

Facebook Ireland Ltd:
31.13.24.0/21
31.13.64.0/18
185.60.216.0/22

Facebook Inc:
199.201.64.0/22
```
