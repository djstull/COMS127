import math
import time


class Clock:
    def __init__(self, days, hours, mins, secs):
        self.d = days
        self.h = hours
        self.m = mins
        self.s = secs
        self._overflow_()

    def _overflow_ (self):
        while self.s > 59:
            self.m += 1
            self.s -= 60

        while self.m > 59:
            self.h += 1
            self.m -= 60

        while self.h > 23:
            self.d += 1
            self.h -= 24

    def _seconds_(self):
        return ((self.d * 24 * 60 * 60) + (self.h * 60 * 60) + (self.m * 60) + self.s)

    def __str__(self):
        return "%d:%02d:%02d:%02d" % (self.d, self.h, self.m, self.s)

    def __add__(self, other):
        t1 = self._seconds_()
        t2 = other._seconds_()
        return Clock(0, 0, 0, t1 + t2)

    def __sub__(self, other):
        t1 = self._seconds_()
        t2 = other._seconds_()
        return Clock(0, 0, 0, t1 - t2)

    def __mul__(self, multi):
        t1 = self._seconds_()
        return Clock(0, 0, 0, math.ceil(t1 * multi))


def main():
        t1 = Clock(0, 23, 59, 59)
        t2 = Clock(0, 0, 0, 1)
        print(t1 + t2)
        print(t1 * 2.5)


if __name__ == '__main__':
    main()
        

