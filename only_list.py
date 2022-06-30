#!usr/bin/env python3

import matplotlib
a = [1, 2, 3, [5, 6, 8, [88, 99, 1]]]
print(list(matplotlib.cbook.flatten(a)))
