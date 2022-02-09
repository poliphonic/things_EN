#!/usr/bin/env python3


def rot13(s):
    inp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    trans = str.maketrans(inp, out)
    return s.translate(trans)


st = 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?'
print(rot13(st))
