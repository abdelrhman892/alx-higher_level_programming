#!/usr/bin/python3
num = 90
con = 0
result = ""

while num >= 65:
    if con == 0:
        result += chr(num + 32)
        con = 1
    else:
        result += chr(num)
        con = 0
    num -= 1

print(result)
