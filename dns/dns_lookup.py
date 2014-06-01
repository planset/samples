import DNS

print(DNS.dnslookup('shinnippon-k.com', 'any', 
    server='technos-hokkaido.co.jp',
    protocol='udp'))
#print(DNS.dnslookup('shinnippon-k.com', 'any', '8.8.8.8'))

