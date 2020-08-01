# -*- coding: UTF-8 -*-
from Crypto.Hash import MD2
import sys

t_1 = "73.25"

def md2E(_str):
    m = MD2.new()
    m.update(_str)
    return m.hexdigest()


if __name__ == '__main__':
    t = t_1
    for i in range(10**8):
        sys.stdout.write("\r%d" % i)
        sys.stdout.flush()
        t = md2E(t.encode(encoding='utf-8'))
    print("\n\n")
    print(t)
