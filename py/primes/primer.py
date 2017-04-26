# -*- coding: utf-8 -*-
import sys
import argparse


class Primer:
    def __init__(self):
        self._iterations_limit = 1000
        self.__prime_numbers = []

    def last(self):
        return self.__prime_numbers[-1] if self.__prime_numbers else None

    def _get_next(self):
        last = self.last()
        if not last:
            return 2
        elif last == 2:
            return 3
        else:
            iter_num = 0
            while iter_num < self._iterations_limit:
                last += 2
                iter_num += 1
                try:
                    next(filter(lambda x: last % x == 0, self.__prime_numbers[1:]))
                except StopIteration:
                    return last
        raise Exception('iterations limit exceeded')


    def next(self):
        result = self._get_next()
        self.__prime_numbers.append(result)
        return result


def main():
    parser = argparse.ArgumentParser(description='calculate prime numbers')
    parser.add_argument('-f', '--first', dest='first', metavar='N', type=int, default=0,
                        help='prints N first prime numbers ')
    parser.add_argument('-s', '--sum', dest='sum', metavar='N', type=int, default=0,
                        help='sums first N prime numbers')
    args = parser.parse_args()

    if args.first > 1:
        p = Primer()
        print('First', args.first, 'primes:', ', '.join((str(p.next()) for i in range(args.first))))
    if args.sum > 0:
        p = Primer()
        print('Sum first', args.sum, 'primes:', sum((p.next() for i in range(args.sum))))


    return 0


if __name__ == '__main__':
    sys.exit(main())