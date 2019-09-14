#简单现行回归：只有一个自变量 y=k*x+b 预测使 (y-y*)^2  最小
import numpy as np

def fitSLR(x,y):
    n=len(x)    #获取x的长度，x是list
    dinominator = 0#初始化分母
    numerator=0     #初始化分子
    for i in range(0,n):    #求b1
        numerator += (x[i]-np.mean(x))*(y[i]-np.mean(y))
        dinominator += (x[i]-np.mean(x))**2 #**表示平方
    print("numerator:"+str(numerator))
    print("dinominator:"+str(dinominator))
    b1 = numerator/float(dinominator)   #得出b1
    b0 = np.mean(y)/float(np.mean(x))   #得出b0
    return b0,b1


# y= b0+x*b1
def prefict(x,b0,b1):       #定义一个简单的线性方程
    return b0+x*b1

x=[1,3,2,1,3]
y=[14,24,18,17,27]
b0,b1=fitSLR(x, y)          
y_predict = prefict(6,b0,b1)
print("y_predict:"+str(y_predict))
