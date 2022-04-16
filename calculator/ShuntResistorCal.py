# 并联电阻计算器, 将任意数量电阻值通过命令函传递即可

import sys

def compute(lst):
    r = sum(map(lambda x:1/x, lst))  #使用map将lambda表达式映射到列表中
    print('\n{0:.8f}\n'.format(1/r))    #一定要保留3位小数


if __name__ == "__main__":
    sys.argv.pop(0)
    if sys.argv:
        arr = map(lambda n:float(n), sys.argv)
        compute(arr)
    else:
        print("\nError\n")
