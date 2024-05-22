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


a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
