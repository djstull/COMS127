
class rational:

    @staticmethod
    def _gcd(first, second):

        if first == 0:
            return second

        if second == 0:
            return first

        if first < second:
            temp = first
            first = second
            second = temp

        return rational._gcd(second, first % second)

    def _to_lowest_terms(self):
        gcd = rational._gcd(self.n, self.d)
        self.n //= gcd
        self.d //= gcd

    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        self._to_lowest_terms()

    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def decimal(self):
        return self.n / self.d

    def __add__(self, other):
        self.n *= other.d
        firstDen = self.d
        self.d *= other.d

        other.n *= firstDen
        other.d *= firstDen

        result = rational(self.n + other.n, self.d)
        return result

    def __sub__(self, other):
        self.n *= other.d
        firstDen = self.d
        self.d *= other.d

        other.n *= firstDen
        other.d *= firstDen

        result = rational(self.n - other.n, self.d)
        return result

    def __mul__(self, other):
        result = rational(self.n * other.n, self.d * other.d)
        return result

    def __truediv__(self, other):
        result = rational(self.n / other.d, self.d / other.n)
        return result


a = rational(1, 4)
b = rational(1, 2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)