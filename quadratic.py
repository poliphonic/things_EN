#!/usr/bin/env python3

def quadratic(a, b, c):
    """
    a, b, c: the numbers from a quadratic equation 
        a * x ** 2 + b * x + c = 0
    return: one or two values of equation or a message about no roots
    """
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1, x2 = (-b + d ** .5) / (2 * a), (-b - d ** .5) / (2 * a)
        return f'x1 = {x1}, x2 = {x2}'
    if d < 0:
        return 'the equation has no roots'
    else:
        return f'x = {-b / (2 * a)}'
