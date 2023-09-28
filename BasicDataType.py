#!/usr/bin/python3

counter = 100   # int
miles = 1000.0  # float
name = "runnoob"    # string

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