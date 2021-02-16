# The App produces the prime numbers in proper range
import math
N = 100
m = 2
index = 0
for i in range(3,N):
    m = 2
    while 1:
        if (i % m) == 0:
            break
        else:
            m = m +1
            if m > i ** 0.5:
                print(i)
                break





