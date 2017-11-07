from fractions import Fraction
c = 1
for i in range(7):
    for j in range(10):
        c *= Fraction(i*10+j+1, j+1)
        print i*10+j+1, j+1
    print c