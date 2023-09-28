#!/usr/bin/python3

counter = 100  # int
miles = 1000.0  # float
name = "runnoob"  # string

print(type(counter))

print(counter)
print(miles)
print(name)

a = b = c = 1

a, b, c = 1, 2, "runnoob"

a = 111
print(isinstance(a, int))

'''
type() 和 isinstance 的区别是：
    type不会认为子类是一种父类类型
    而isinstance会认为子类是一种父类类型
'''

var = 1
del var

# !/usr/bin/python3

str1 = 'Runoob'

print(str1)  # 输出字符串
print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str1[0])  # 输出字符串第一个字符
print(str1[2:5])  # 输出从第三个开始到第五个的字符
print(str1[2:])  # 输出从第三个开始的后的所有字符
print(str1 * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str1 + "TEST")  # 连接字符串

print('Ru\noob')
print(r'Ru\noob')  # 使用 r 可以使其不转义

word = 'Python'
print(word[0])
# word[1] = 'r'


#   Bool 类型
# Ture or False
a = True
b = False

# 比较运算符
print(2 < 3)
print(2 == 3)

# 逻辑运算符
print(a and b)
print(a or b)
print(not a)

# 类型转换
print(int(a))
print(float(b))
print(str(a))

##### 列表
# 写在 【】之间，使用，隔开
# 索引以0为开始值，-1为末尾的开始位置

list = ['abcd', 768, 2.23, 'runnob', 70.2]
tinylist = [123, 'runnoob']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list + tinylist)



