
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tentwen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

numdict = {}

for i in range(1, 10):
    numdict[i] = len(ones[i - 1])

for i in range(10, 20):
    numdict[i] = len(tentwen[i - 10])

for i in range(2, 10):
    numdict[i * 10] = len(tens[i - 2])
    for j in range(1, 10):
        numdict[i * 10 + j] = len(tens[i - 2]) + len(ones[j - 1])

for i in range(1, 10):
    numdict[i * 100] = len(ones[i - 1]) + 7 # i hundred
    for j in range(1, 100):
        numdict[i * 100 + j] = len(ones[i - 1]) + 10 + numdict[j] # i + hundred and + smth

numdict[1000] = 11 # one thousand

numsum = 0
for key, value in numdict.items():
    numsum += value
    print(key, value, numsum)
