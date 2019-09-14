import math
def calculate(x,y):
    n = len(x)
    #计算 x的平均数
    x_sum = 0
    for x_j in x:
        x_sum = x_sum + x_j
    x_arrange = x_sum / n
    #计算 y的平均数
    y_sum = 0
    for y_j in y:
        y_sum = y_sum + y_j
    y_arrange = y_sum / n
    #
    i = 0
    xiyi_sum = 0
    xi_square_sum = 0
    yi_square_sum = 0
    while i < n:
        xiyi_sum = xiyi_sum + x[i]*y[i]
        xi_square_sum = xi_square_sum + x[i]**2
        yi_square_sum = yi_square_sum + y[i]**2
        i = i + 1
    #计算分子与分母，以及 b,a,r
    numerator = xiyi_sum - n*x_arrange*y_arrange
    denominator_1 = xi_square_sum - n*pow(x_arrange,2)
    denominator_2 = math.sqrt(denominator_1 * (yi_square_sum - n*pow(y_arrange,2)))
    b = numerator / denominator_1
    a = y_arrange - b*x_arrange
    r = numerator / denominator_2
    #
    return [x_arrange,y_arrange,xiyi_sum,xi_square_sum,numerator,denominator_1,denominator_2,b,a,r]


def predict():
    print("预测(多个数用空格隔开)：")
    x_input = input("x = ")
    x_input = [float(n) for n in x_input.split()]
    y_output = []
    for x_in in x_input:
        y_out = b*x_in + a
        y_output.append(y_out)
    print("y = "+str(y_output))
    print("\n===========================\n")
    return [x_input,y_output]

def draw():
    import matplotlib.pyplot as plt
    import numpy as np
    #画散点图
    plt.scatter(x,y,s=25,color="blue",label="Raw")
    plt.scatter(results_predict[0],results_predict[1],s=35,color="red",marker="^",label="Predict")
    #画直线
    #合并原始数据，预测数据两个数组作为 x轴（变量名 x_s）
    x_s = x +results_predict[0]
    #用 np.arange 生成自变量范围：x轴中最小值-3 到 x轴中最大值+3，步长：1
    xdata = np.arange(min(x_s)-3,max(x_s)+3,1)
    ydata = b*xdata + a #回归方程
    plt.plot(xdata,ydata,color="green")
    # 设置图表标题， 并给坐标轴加上标签
    plt.title("Title", fontsize=24)
    plt.xlabel("x-value", fontsize=14)
    plt.ylabel("y-value", fontsize=14)
    plt.legend(loc="best") # 设置图例位置
    plt.savefig("./result.png")
    plt.show()


#定义原始数据
x = [1,2,3,4,5,6,8]
y = [-5,-7,-6,-9,-12,-11,-15]
#调用 “计算”，接受返回参数
results = calculate(x,y)
b = results[7]
a = results[8]
r = results[9]
#输出信息
print("===========================\n")
print("x = "+str(x))
print("y = "+str(y))
print("x_arrange= "+str(results[0]))
print("y_arrange= "+str(results[1]))
'''
print("xiyi_sum= "+str(results[2]))
print("xi_square_sum= "+str(results[3]))
print("numerator= "+str(results[4]))
print("denominator_1 = "+str(results[5]))
print("denominator_2 = "+str(results[6]))
'''
if a >= 0:
    print("\ny = "+str(b)+"x + "+str(a))
else:
    print("\ny = "+str(b)+"x "+str(a))
print("r = "+str(r))
print("\n===========================\n")
#调用 “预测”
results_predict = predict()
#交互 是否作图
c = input("是否作图？(y/n)：")
if c == "y" or c == "Y":
    print("\n开始作图……")
    draw()
else:
    print("\n跳过作图\n")
#
print("\n===========================\n")
print("运行完毕")
