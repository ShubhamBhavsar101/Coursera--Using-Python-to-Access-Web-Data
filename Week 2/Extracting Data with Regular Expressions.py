import re

regex = input("Enter the file name")
if len(regex) < 1: regex = "regex_sum_832134.txt"

fh = open(regex)
lines = fh.read()
sumlist = re.findall('[0-9]+', lines)

sum = 0
for no in sumlist:
    sum = sum + int(no)

print(sum)