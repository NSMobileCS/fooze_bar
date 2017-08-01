"""
for numbers 100 to 100000 (100K)
    test whether it's prime or a perfect square
      if prime print 'Foo'
      if perfect square print 'Bar'
      if neither print 'FooBar!'
"""

def isPerfectSquare(n):
    x = int(n**.5)
    return x**2 == n

class Primes:
    def __init__(self, value):
        self.arr = [2, 3]
        for n in range(3, value):
            self.isPrimeNumber(n)

    def isPrimeNumber(self, n):
        if n in self.arr:
            return True
        for prime in self.arr:
            if n % prime == 0:
                return False
        self.arr.append(n)
        return True


def fooBar(startval=100, endval=100000, return_list=False):
        if return_list:
            rl = []
        print(startval)
        primes = Primes(100)
        for n in range(100, endval+1):
            result = ''
            if primes.isPrimeNumber(n):
                result = 'Foo'
            elif isPerfectSquare(n):
                result = 'Bar'
            else:
                result = 'FooBar!'
            if return_list:
                rl.append((n, result))
            else:
                print(str(n) + ' \t ' + result)
        if return_list:
            return rl

fooBar()