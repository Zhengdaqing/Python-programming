#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python Keywrods
import keyword
print(keyword.kwlist)


# In[43]:


#合法的变量标识符
variable_1 = 5
name = 'Mike'
total_sum = 0

# 合法的函数名
def calculate_sum(num1, num2):
    return num1 + num2

# 合法的类名
class SampleClass:
    pass


# In[44]:


# 变量赋值
import math

radius = 100
area = math.pi * radius **2
print(area)

st = "I am a professor of SUFE."
print(st)


# In[45]:


# 用解包赋值实现两个变量的值交换
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)


# In[46]:


Name = input('please input your name:')
Salary = float(input('please input your monthly salary:'))
# 从单个输入中同时获取两个数据
Name, age = input('please input your name and age, separated by spaces:').split()
print('you name is', Name, 'and you age is', age)


# In[51]:


name = 'Alice'
salary = 5000
# 通过str.format()来对结果进行格式化，它使用大括号’{}’作为占位符
print("The salary of {} is {}".format(name, salary))
# The salary of Alice is 5000 yuan.

# 在字符串前添加f来完成格式化字符串字面量
print(f"The salary of {name} is {salary} yuan.")
# The salary of Alice is 5000 yuan.

# 在大括号中指定不同格式化选项
print("{:0>3d}".format(5))  # 005

print("{:.2f}".format(3.14159))  # 3.14


# In[ ]:


# 使用for循环逐行读取
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end=' ')
# 使用write()方法写入文件
with open('example.txt', 'w') as file:
    file.write("Hello World\n")


# In[57]:


type(-2)  # Int

int("-5") # 将字符串类型转化为整数类型，结果是-5

int(2.5) # 将浮点数类型转化为整数类型，结果是2

large_int = 12345678987654321 # 一个很大的整数可以被创建

type(-0.333) # float

float("3.1415926") # 将字符串类型转化为浮点数类型，3.1415926

float(-5) # 将整数类型转化为浮点数类型，-5.0


# In[58]:


print(0.1+0.2)  # 0.30000000000000004
print(0.1+0.2 ==0.3)  # False


# In[5]:


print(0.1+0.2)
print(0.1+0.2 ==0.3)


# In[6]:


# 非常大的数
large_number = 12345678901234567890.0
print(large_number)  # 输出: 1.2345678901234568e+19

# 非常小的数
small_number = 0.000000000000000000123456789
print(small_number)  # 输出: 1.23456789e-19


# In[7]:


large_number = 1.2345678901234567e+19
print(large_number)


# In[9]:


#ch2-1
money = eval(input("输入金额："))
m50 = money // 50
money = money% 50
m5 = money // 5
money = money % 5
m1 = money
print("50元面额的人民币需要的张数：", m50)
print("5元面额的人民币需要的张数：", m5)
print("1元面额的人民币需要的张数：", m1)


# In[1]:


import math
print(math.pi) # 3.141592653589793


# In[2]:


from math import pi
print(pi) # 3.141592653589793


# In[6]:


#ch2-2
name = "Daqing"
greeting = "hello, " + name
print(greeting) # hello, Daqing


# In[5]:


greeting = "Hello world"
print(greeting[0]) # H 
print(greeting[-11]) # H
print(greeting[-1]) # d
print(greeting[10]) # d


# In[22]:


greeting = "Hello Mike"
print(greeting[0:11:1]) # Hello Mike
print(greeting[11:0:-1]) # ekiM olle
print(greeting[4::-1]) # olleH
print(greeting[::-1]) # ekiM olleH
print(greeting[::-3]) # eMlH


# In[27]:


#ch2-5
m = int(input("输入一个0～12间的整数："))
months="JanFebMarAprMayJunJulAugSepoctNovDec"
pos = (m-1)*3
print(months[pos: pos+3])


# In[33]:





# In[8]:


#ch2-6
s = "I am a professor in University"
print(len(s))
print(str(3+5))
print(hex(62))
print(oct(62))


# In[14]:


#ch2-7
print(ord('A'), ord('B'), ord('C')) #A,B,C的Unicode编码分别为65,66和67
print(ord('a'), ord('b'), ord('c')) #a,b,c的Unicode编码分别为97,98和99
print(ord('0'), ord('1'), ord('2')) #数字0,1,2的Unicode编码分别为48,49和50
print(ord('/'), ord('+'), ord(' ')) #字符/,+,空格的Unicode编码分别为47,43和32
print(chr(97), chr(98), chr(99)) #Unicode编码为97,98和99的字符分别是a,b和c


# In[23]:


#ch2-8
s = "bird, fish, monkey, rabbit"
print(s.find('fish')) #结果为6
print(s.rfind('b')) #结果为23
print(s.index('fish')) #结果为6
print(s.rindex('b')) #结果为23
print(s.count('b')) #结果为3


# In[14]:


#ch2-9
s = "bird, fish, monkey, fish, rabbit"
print(s.split(",")) # 按照‘，’分隔字符串
city = "北京 上海 广州 深圳 杭州"  
print(city.split()) # 默认按照空格分隔字符串
print(city.split(maxsplit =2)) #从左开始，最多分隔2次，分出‘北京’和‘上海’
print(city.rsplit(maxsplit =2)) #从右开始，最多分隔2次，分出‘深圳’和‘杭州’
print(s.partition('fish')) #按左端第一个fish将字符串分成3个部分
print(s.rpartition('fish')) #按右端第一个fish将字符串分成3个部分
print(s.partition('tiger')) # 分隔符不存在，则返回原字符串和2个空字符串


# In[15]:


#ch2-10
li = ['apple', 'banaba', 'pear', 'peach'] # li是链表数据类型，
print(':'.join(li)) # 用‘：’作为连接符，结果为'apple:banaba:pear:peach'
print('-'.join(li)) #用‘-’作为连接符，结果为'apple-banaba-pear-peach'


# In[17]:


#ch2-11
s = "I am a professor of SUFE"
print(s.lower()) # 返回小写字符串
print(s.upper()) # 返回大写字符串
print(s.capitalize()) # 首字母大写字符串
print(s.title()) # 返回每个单词首字母大写的字符串
print(s.swapcase()) # 返回大小写互换字符串


# In[19]:


#ch2-12
s = "I am a professor of SUFE"
s.replace('professor','student') # 输出'I am a student of SUFE'


# In[23]:


#ch2-13
s = "====Mike===="
print(s.strip('=')) # Mike
print(s.rstrip('=')) # ====Mike
print(s.lstrip('=')) # Mike====


# In[27]:


#ch2-14
s = "I am a professor of SUFE"
print(s.startswith("I an")) # 检测字符串是否以‘I an’开始，输出结果False
print(s.endswith("SUFE")) # 检测字符串是否以‘SUFE’结束，输出结果True


# In[35]:


#ch2-15
s = 'years'
print(s.islower()) # 判断字符串是否为全小写，返回True
s = 'YEARS'
print(s.isupper()) # 判断字符串是否为全大写，返回True
s = '20241122'
print(s.isdigit()) # 判断字符串是否为全数字，返回True
s = 'He is 10 years old'
s = s.replace('','') # 去除字符串中的空格
print(s.isalnum()) # 判断字符串是否为全数字，返回False
print(s.isalpha()) # 判断字符串是否为全字母，返回False


# In[38]:


#ch2-16
s = 'Hello Mike'
print(s.center(30,'=')) # 字符串居中对齐，输出宽度为30，不足的以'='填充
print(s.ljust(20,'*')) # 字符串居左对齐，输出宽度为20，不足的以'*'填充
print(s.rjust(20,'*')) # 字符串居右对齐，输出宽度为20，不足的以'*'填充
print(s.zfill(20))  # 输出宽度为20，在字符串左侧以字符'0'填充


# In[59]:


#ch2-17
print("我是{}学院{}专业的学生。".format("信息管理与工程","信息管理"))
print("我是{1}学院{2}专业的学生{0}。".format("郑砺","信息管理与工程","信息管理"))


# In[44]:


#ch2-18 format()函数格式化字符串
print("{:*^20}".format("Mike"))
print("{:=<20}".format("Mike"))


# In[60]:


#ch2-19 format()函数设置格式
print("{:.2f}".format(3.1415926))
print("{:=^30.4f}".format(3.141592))
print("{:5d}".format(24))
print("{:x>5d}".format(24))


# In[1]:


#ch2-20 布尔运算应用于条件判断
a = 10
b = 20

print(a == b)  # False

# 布尔运算应用于逻辑运算
x = True
y = False
print(x and y) # False


# In[ ]:




