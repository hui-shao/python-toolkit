from datetime import datetime
import traceback
from functools import wraps
import requests


def a_decorator(_func):
    def wrap(*args, **kwargs):  # *args, **kwargs 是 _func 的参数列表
        print("Before executing the func")
        ret = _func(*args, **kwargs)
        print("After executing the func\n")
        return ret

    return wrap


def except_wrap(msg="Details"):
    """
    异常处理装饰器
    :param msg: 用于自定义输出的提示异常的信息
    :return:
    """

    def except_execute(_func):
        @wraps(_func)  # 不改变使用装饰器原有函数的结构(如__name__, __doc__)
        def except_catch(*args, **kwargs):
            try:
                print("Before executing the func")
                ret = _func(*args, **kwargs)  # ret 记录原函数返回值
            except ValueError:
                print("Value Error")
                return -2
            except Exception as e:
                sign = '=' * 60 + '\n'
                print(f'{sign}>>> Time: \t{datetime.now()}\n>>> Function: \t{_func.__name__}\n>>> {msg}: \t{e}')
                print(f'{sign}{traceback.format_exc()}{sign}')
                return -1
            else:
                return ret
            finally:
                print("After executing the func\n\n")

        return except_catch

    return except_execute


def requests_except(msg="Error INFO"):
    """
    requests 异常处理装饰器
    :param msg: 用于自定义输出的提示异常的信息
    :return:
    """

    def except_execute(_func):
        @wraps(_func)
        def except_catch(*args, **kwargs):
            for retry_n in range(0, 5):
                try:
                    ret = _func(*args, **kwargs)
                except requests.exceptions.SSLError:
                    logging.error("SSL 错误, 2s后重试 -> SSLError: An SSL error occurred.")
                    time.sleep(2)
                except requests.exceptions.ConnectTimeout:
                    logging.error(
                        "建立连接超时, 5s后重试 -> ConnectTimeout: The request timed out while trying to connect to the remote server.")
                    time.sleep(5)
                except requests.exceptions.ReadTimeout:
                    logging.error(
                        "读取数据超时, 3s后重试 -> ReadTimeout: The server did not send any data in the allotted amount of time.")
                    time.sleep(3)
                except requests.exceptions.ConnectionError:
                    logging.error(f"{traceback.format_exc(3)}")
                    logging.error("建立连接错误, 5s后重试", front="\n")
                    time.sleep(5)
                except requests.exceptions.RequestException:
                    logging.error(f"{traceback.format_exc(3)}")
                    logging.error("其他网络连接错误, 5s后重试", front="\n")
                    time.sleep(5)
                except KeyboardInterrupt:
                    logging.warning("捕获到 KeyboardInterrupt, 退出", front="\n")
                    return None
                except Exception as e:
                    sign = '=' * 60 + '\n'
                    print(f'{sign}>>> Time: \t{datetime.now()}\n>>> Function: \t{_func.__name__}\n>>> {msg}: \t{e}')
                    print(f'{sign}{traceback.format_exc()}{sign}')
                    return None
                else:
                    return ret
                finally:
                    pass
                continue
            logging.error("\n达到最大重试次数, 退出")
            return None

        return except_catch

    import time
    import logging
    logging.basicConfig(level=logging.INFO)
    return except_execute


@a_decorator
def test(n: int):
    print("This is a test. The num is %d" % n)

# 装饰器的作用相当于 执行了
# test = a_decorator(test)
# 装饰器只在声明时执行一次
# 此后调用 test 时 都会调用被爆炸好的 test


@except_wrap()  # 此装饰器需要加上括号进行调用
def test1(n: int):
    if n == 3:
        raise ValueError
    print(6 / n)
    return 5


if __name__ == '__main__':
    test(1)
    a = test1(5)
    b = test1(0)
    c = test1(3)
    print("{},{},{}".format(a, b, c))
