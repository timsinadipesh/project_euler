# find the sum of all the numbers that 
# can be written as the sum of fifth powers
# of their digits

tot = 0
for i in range(10, 10 ** 7 + 1):
    st = str(i)
    dig_tot = 0
    for c in st:
        dig_tot += (int(c)) ** 5
    if dig_tot == i:
        tot += dig_tot
        print(dig_tot, i)
print(tot)