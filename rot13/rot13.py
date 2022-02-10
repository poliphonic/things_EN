#!/usr/bin/env python3


def rot13(s):
    """
    s: a string
    return: translated in rot13 cipher s
    """
    inp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    return s.translate(str.maketrans(inp, out))


st = 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?'
print(rot13(st))
