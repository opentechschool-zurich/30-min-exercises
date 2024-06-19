barcode = 7649988281129

checksum = barcode % 10
barcode = barcode // 10

print(barcode, checksum)

odd = True

summe = 0

while barcode > 0:
    # summe += (barcode % 10) * (odd * 2 + 1)
    summe += (barcode % 10) * (3 if odd else 1)
    barcode = barcode // 10
    odd = not odd

print((10 - summe % 10) % 10 == checksum)
