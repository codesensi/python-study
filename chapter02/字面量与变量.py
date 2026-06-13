# 字面量的写法
print(1)  # 整数(int)
print(3.1415926)  # 浮点数(float)
print(True)  # 布尔值(bool)
print(False)  # 布尔值(bool)
print("hello python")  # 字符串(str)
print(None)  # 空值(NoneType)

# 布尔类型的本质是整数(True=1;False=0)
print(True + 1)
print(False - 1)

print("---------以上是字面量----------")

print("---------以下是变量----------")

# 变量的写法
num = 12345.67
print(num)

num = 5214.7
print(num)

num = num + 1
print(num)

# python是动态类型语言，在程序运行时才进行类型检查，变量的类型可以在程序运行过程中改变，即一个变量可以接受不同类型的值
num = "python good"
print(num)

# 一次性定义多个变量
a, b, c = 1, 2, 3
print(a, b, c)
