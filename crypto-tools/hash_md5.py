import hashlib
import sys

str_1 = '这是测试'  # 需要加密的文本
n = 100000000  # 加密次数
if __name__ == '__main__':
    str_md5 = hashlib.md5(str_1.encode(encoding='utf-8')).hexdigest()
    for i in range(n - 1):
        str_md5 = hashlib.md5(str_md5.encode(encoding='utf-8')).hexdigest()
        sys.stdout.write('\r%d' % i)
        sys.stdout.flush()
    print('\n\n')
    print(str_md5)
