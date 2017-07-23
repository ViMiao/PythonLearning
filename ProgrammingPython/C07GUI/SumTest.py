import math
s = 1.0
for i in range(1, 1000000000):
    s = s + 1/2**i + 1/3**i;

print(s)