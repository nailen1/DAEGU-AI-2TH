price = float(input('가격?'))
taxrate = 0.1
vat = price * taxrate
print(vat)

f = open('result.txt', 'a')
f.write(str(vat)+'\n')
f.close()
