"""
str = "12345678"
st = "".join(reversed(str[:-1]))
"""
import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

while len(b) > len(a):
    if b[-1] == "A":
        b = b[:-1]
    else:
        b = "".join(reversed(b[:-1]))

if a == b:
    print(1)
else:
    print(0)
