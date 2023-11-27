#!/usr/bin/env python3

from sequences import print_fibonacci

class TestPrintFibonacci:
    '''function print_fibonacci()'''

    def test_print_fibonacci_zero(self):
        '''prints empty list when length = 0'''
        result = print_fibonacci(0)
        assert result == []

    def test_print_fibonacci_one(self):
        '''prints 0 when length = 1'''
        result = print_fibonacci(1)
        assert result == [0]

    def test_print_fibonacci_two(self):
        '''prints 0\\n1 when length = 2'''
        result = print_fibonacci(2)
        assert result == [0, 1]

    def test_print_fibonacci_ten(self):
        '''prints 0\\n1\\n1\\n2\\n3\\n5\\n8\\n13\\n21\\n34 when length = 10'''
        result = print_fibonacci(10)
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
