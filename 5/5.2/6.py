import math


class Fraction():
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.num, self.denom = map(int, args[0].split('/'))
        else:
            self.num, self.denom = args[0], args[1]
        self.__gcd()

    def __sign(self):
        if self.num < 0:
            return -1
        return 1

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __gcd(self):
        gcd = math.gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd

        if self.denom < 0:
            self.num = -self.num
            self.denom = abs(self.denom)
        return self

    def __str__(self) -> str:
        return f'{self.num}/{self.denom}'

    def __repr__(self) -> str:
        return f"Fraction('{self.num}/{self.denom}')"

    def numerator(self, *args):
        if len(args):
            self.num = args[0] * self.__sign()
            self.__gcd()
        return abs(self.num)

    def denominator(self, *args):
        if len(args):
            self.denom = args[0]
        self.__gcd()
        return abs(self.denom)

    def __add__(self, other):
        tmp_denom = self.denom * other.denom
        tmp_num = self.num * other.denom + other.num * self.denom
        return Fraction(tmp_num, tmp_denom)

    def __iadd__(self, other):
        tmp_num = self.num
        tmp_denom = self.denom
        self.denom = tmp_denom * other.denom
        self.num = tmp_num * other.denom + other.num * tmp_denom
        self.__gcd()
        return self

    def __sub__(self, other):
        tmp_denom = self.denom * other.denom
        tmp_num = self.num * other.denom - other.num * self.denom
        return Fraction(tmp_num, tmp_denom)

    def __isub__(self, other):
        tmp_num = self.num
        tmp_denom = self.denom
        self.denom = tmp_denom * other.denom
        self.num = tmp_num * other.denom - other.num * tmp_denom
        self.__gcd()
        return self

a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
