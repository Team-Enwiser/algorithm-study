#4619

import sys
import math

for line in sys.stdin:
    b, n = map(int, line.split())
    if(n == 0):
        continue
    x = math.ceil(b**(1/n))
    y = math.floor(b**(1/n))
    xx = abs(x ** n - b)
    yy = abs(y ** n - b)

    if xx > yy:
        print(y)
    else:
        print(x)