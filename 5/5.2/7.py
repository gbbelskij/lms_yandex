import math


class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            if '/' in args[0]:
                self.num, self.denom = map(int, args[0].split('/'))
            else:
                self.num = int(args[0])
                self.denom = 1
        elif isinstance(args[0], Fraction):
            self.num = args[0].num
            self.denom = args[0].denom
        elif len(args) > 1:
            self.num, self.denom = args[0], args[1]
        else:
            self.num = args[0]
            self.denom = 1
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
        oth = Fraction(other)
        tmp_denom = self.denom * oth.denom
        tmp_num = self.num * oth.denom + oth.num * self.denom
        return Fraction(tmp_num, tmp_denom)

    def __radd__(self, other):
        oth = Fraction(other)
        tmp_denom = self.denom * oth.denom
        tmp_num = self.num * oth.denom + oth.num * self.denom
        return Fraction(tmp_num, tmp_denom)

    def __iadd__(self, other):
        oth = Fraction(other)
        tmp_num = self.num
        tmp_denom = self.denom
        self.denom = tmp_denom * oth.denom
        self.num = tmp_num * oth.denom + oth.num * tmp_denom
        self.__gcd()
        return self

    def __sub__(self, other):
        oth = Fraction(other)
        tmp_denom = self.denom * oth.denom
        tmp_num = self.num * oth.denom - oth.num * self.denom
        return Fraction(tmp_num, tmp_denom)

    def __rsub__(self, other):
        oth = Fraction(other)
        tmp_denom = self.denom * oth.denom
        tmp_num = oth.num * self.denom - self.num * oth.denom
        return Fraction(tmp_num, tmp_denom)

    def __isub__(self, other):
        oth = Fraction(other)
        tmp_num = self.num
        tmp_denom = self.denom
        self.denom = tmp_denom * oth.denom
        self.num = tmp_num * oth.denom - oth.num * tmp_denom
        self.__gcd()
        return self

    def __mul__(self, other):
        oth = Fraction(other)
        return Fraction(self.num * oth.num, self.denom * oth.denom)

    def __rmul__(self, other):
        oth = Fraction(other)
        return Fraction(self.num * oth.num, self.denom * oth.denom)

    def __imul__(self, other):
        oth = Fraction(other)
        self.num *= oth.num
        self.denom *= oth.denom
        self.__gcd()
        return self

    def __truediv__(self, other):
        oth = Fraction(other)
        return Fraction(self.num * oth.denom, self.denom * oth.num)

    def __rtruediv__(self, other):
        oth = Fraction(other)
        return Fraction(oth.num * self.denom, oth.denom * self.num)

    def __itruediv__(self, other):
        oth = Fraction(other)
        self.num *= oth.denom
        self.denom *= oth.num
        self.__gcd()
        return self

    def reverse(self):
        return Fraction(self.denom, self.num)

    def __gt__(self, other):
        oth = Fraction(other)
        if self.num / self.denom > oth.num / oth.denom:
            return True
        return False

    def __lt__(self, other):
        oth = Fraction(other)
        if self.num / self.denom < oth.num / oth.denom:
            return True
        return False

    def __ge__(self, other):
        oth = Fraction(other)
        if self.num / self.denom >= oth.num / oth.denom:
            return True
        return False

    def __le__(self, other):
        oth = Fraction(other)
        if self.num / self.denom <= oth.num / oth.denom:
            return True
        return False

    def __eq__(self, other):
        oth = Fraction(other)
        if self.num == oth.num and self.denom == oth.denom:
            return True
        return False

    def __ne__(self, other):
        oth = Fraction(other)
        if self.num == oth.num and self.denom == oth.denom:
            return False
        return True


a = Fraction(1)
b = Fraction('2')
c, d = map(Fraction.reverse, (2 + a, -1 + b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
