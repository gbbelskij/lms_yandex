import math


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.denom = map(int, args[0].split('/'))
        else:
            self.num, self.denom = args[0], args[1]
        self.__gcd()

    def __gcd(self):
        gcd = 2
        while gcd > 1:
            gcd = math.gcd(self.num, self.denom)
            self.num //= gcd
            self.denom //= gcd

    def numerator(self, *args):
        if len(args) == 0:
            return self.num
        else:
            self.num = args[0]
            self.__gcd()

    def denominator(self, *args):
        if len(args) == 0:
            return self.denom
        else:
            self.denom = args[0]
            self.__gcd()

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.denom})"
