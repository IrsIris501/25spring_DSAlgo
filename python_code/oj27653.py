class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator
    def prt(self):
        print('{}/{}'.format(self.numerator, self.denominator))
import math
def add(frac1, frac2):
    numerator1=frac1.numerator
    numerator2=frac2.numerator
    denominator1=frac1.denominator
    denominator2=frac2.denominator
    numerator1 *= denominator2 // math.gcd(denominator1, denominator2)
    numerator2 *= denominator1 // math.gcd(denominator1, denominator2)
    num3=numerator2+numerator1
    den3=denominator1*denominator2//math.gcd(denominator1, denominator2)
    num3 = num3 // math.gcd(num3, den3)
    den3 = den3 // math.gcd(num3, den3)
    frac3=Fraction(num3, den3)
    return frac3

a, b, c, d=map(int, input().split())
frac1=Fraction(a, b)
frac2=Fraction(c, d)
add(frac1, frac2).prt()

