# The App produces the prime numbers in proper range
import math
N = 1000
index = 0
file  = open('prime.txt','a+')
for i in range(3,N):
    m = 2
    while 1:
        if (i % m) == 0:
            break
        else:
            m = m +1
            if m > i ** 0.5:
                print(i, end = ' ')
                print(i, file = file, end = ' ')
                break
file.close()





