import numpy as np
import matplotlib.pyplot as plt
#载入数据
#创建数组表格数据，主要执行两个循环。第一个将文件的每一行转换成字符串。第二个将每个字符串转换为相应的数据类型。
data=np.genfromtxt("data.csv",delimiter=",")  

x_data=data[:,0]
print(type(x_data))
y_data=data[:,1]
plt.scatter(x_data,y_data)   #绘制散点图
plt.show()
print(x_data)
#学习率
lr=0.0001
#初始斜率
k=0
#初始截距
b=0
#最大迭代次数
epochs=50

#计算损失
def compute_error(b,k,x_data,y_data):
    totalError=0
    for i in range(0,len(x_data)):
        totalError+=(y_data[i]-(k*x_data[i]+b))**2    
    return totalError/float(len(x_data))/2

def gradient_descent_runner(x_data,y_data,b,k,lr,epochs):
    #计算总数据量
    m=float(len(x_data))
    #循环epochs次
    for i in range(epochs):
        b_grad=0
        k_grad=0
        #计算梯度的总和再求平均
        for j in range(0,len(x_data)):
            b_grad += (1/m)*(((k*x_data[j])+b)-y_data[j])
            k_grad += (1/m)*x_data[j]*(((k*x_data[j])+b)-y_data[j])
        #更新b和k
        b=b-(lr*b_grad)
        k=k-(lr*k_grad)
        # 每迭代5次，输出一次图像
        if i % 5==0:
            print("epochs:",i)
            plt.plot(x_data, y_data, 'b.')
            plt.plot(x_data, k*x_data + b, 'r')
            plt.show()
    return b,k       
        

print("Starting b = {0}, k = {1}, error = {2}".format(b, k, compute_error(b, k, x_data, y_data)))
print("Running...")
b, k = gradient_descent_runner(x_data, y_data, b, k, lr, epochs)
print("After {0} iterations b = {1}, k = {2}, error = {3}".format(epochs, b, k, compute_error(b, k, x_data, y_data)))

#画图
plt.plot(x_data, y_data, 'b.')
plt.plot(x_data, k*x_data + b, 'r')
plt.show()