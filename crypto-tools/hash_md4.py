# -*- coding: UTF-8 -*-
from Crypto.Hash import MD4
import sys

t_1 = "混元一气上方太乙金仙美猴王齐天大圣斗战胜佛孙性空"
t_2 = "孙性空"

def md4E(_str):
    m = MD4.new()
    m.update(_str)
    return m.hexdigest()


if __name__ == '__main__':
    c = t_2
    for i in range(10**8):
        sys.stdout.write("\r%d" % i)
        sys.stdout.flush()
        c = md4E(c.encode(encoding='utf-8'))
    print("\n\n")
    print(c)
