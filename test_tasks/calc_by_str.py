# expected regular phrase, like "2+2*5", and return calculation result "12"
import re


def calc(num):
    num = sum(map(int, re.findall(r'[+-]?\d+', num)))
    return num

a = calc(input())
print(a)