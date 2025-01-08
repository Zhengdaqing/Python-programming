#!/usr/bin/env python
# coding: utf-8

# # 第三章程序

# In[ ]:


a, b = 10, 50
print(0<a<b) # 表示a>0并且b>a，结果为True
print(a==b) # 表示a和b的值是否相等，结果为False
print('ABC'>'abc') # 字符串对应的Unicode编码进行比较，结果为False
print('Python'<'python') # 字符串对应的Unicode编码进行比较，结果为True
print(a >'BC') # TypeError: '>' not supported between instances of 'int' and 'str'


# In[ ]:


a, b = 10, 50
print(a>10 and b<100) # 表示a>10并且b<100，结果为False
print(a>10 or b<100) # 表示a>10或者b<100,结果为True
print(not(a>10 and b<100)) # 将a>10并且b<100的结果取反，最终结果为True


# In[ ]:


bool(123),bool("abc"),bool((1,2)),bool([0]),bool(0) # (True, True, True, True, False)


# In[ ]:


bool(1>2),bool(1>2 or 3>2), bool(1<=2 and 3>2) # (False, True, True)


# In[ ]:


#ch3-1 输入三角形三条边的长度，计算三角形的面积。
import math 
a = float(input('Please input the length of side a of a triangle:'))
b = float(input('Please input the length of side b of a triangle:'))
c = float(input('Please input the length of side c of a triangle:'))
h = (a+b+c)/2
area = math.sqrt(h*(h-a)*(h-b)*(h-c))
print('the area of a triangle is:{:.2f}'.format(area))


# In[ ]:


#ch3-2 
a = int(input('请输入整数a:')) # 提示输入整数a
b = int(input('请输入整数b:')) # 提示输入整数b
print('输入值a = {}, b={}'.format(a, b))  # 输出整数a,b
if a < b:  # 比较a和b,如果a小于b,则交换a，b的值
    a, b = b, a
print('比较后的值 a = {}, b={}'.format(a,b)) # 输出整数a，b


# In[ ]:


#ch3-2 PM2.5空气质量提示
PM25 = eval(input('请输入PM2.5数值：'))
if 0 <=PM25 <35:
    print('空气质量为 优！')
if 35<=PM25 <75:
    print('空气质量为 良！')
if 75<=PM25 < 115:
    print('空气质量为 轻度污染！')
if 115<=PM25 <150:
    print('空气质量为 中度污染！')
if 150<=PM25 <250:
    print('空气质量为 重度污染！')
if 250<=PM25 <500:
    print('空气质量为 严重污染！')


# In[ ]:


#ch3-3 
import math
a = float(input("请输入三角形的边长a："))
b = float(input("请输入三角形的边长b："))  
c = float(input("请输入三角形的边长c："))  
if (a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0):
    h = (a+b+c)/2
    area = math.sqrt(h*(h-a)*(h-b)*(h-c))
    print("三角形的面积为：{:.2f}".format(area))
else:
    print("用户输入数据有误！")


# In[ ]:


x = eval(input('请输入x的值:'))
print(x) if x>=0 else print(-x)


# In[ ]:


#ch3-4 采用多分支选择结构实现PM2.5空气质量提示
PM25 = eval(input('请输入PM2.5数值：'))
if 0 <=PM25 <35:
    print('空气质量为 优！')
elif 35<=PM25 <75:
    print('空气质量为 良！')
elif 75<=PM25 < 115:
    print('空气质量为 轻度污染！')
elif 115<=PM25 <150:
    print('空气质量为 中度污染！')
elif 150<=PM25 <250:
    print('空气质量为 重度污染！')
elif 250<=PM25 <500:
    print('空气质量为 严重污染！')
else: print('空气质量爆表！')


# In[16]:


#ch3-5 使用键盘输入一个3位的正整数，输出其中的最大1位数
st = input("请输入一个3位正整数：")
a = int(st[0])
b = int(st[1])
c = int(st[2])

if a>=b:
    if a>c:
        max_num = a
    else:
        max_num = c
else:
    if b>=c:
        max_num = b
    else:
        max_num = c
print(st + '中最大的1位数字是：',  max_num)


# In[19]:


#ch3-6
# 交易日志，每行1个交易记录，格式"日期, 股票代码, 成交价格, 成交量"
trade_log = """2024-12-15, AAPL, 175.32, 100
2024-12-15, MSFT, 289.45, 150
2024-12-16, AAPL, 176.10, 200
2024-12-16, MSFT, 290.10, 120"""
# 初始化变量用于存储统计数据
total_volume = 0
highest_price = 0
lowest_price = float('inf')
number_of_trades = 0
price_dict = {}
# 使用 for 循环迭代字符串中的每一行
for line in trade_log.splitlines():
    # 忽略空行
    if not line.strip():
        continue
    # 解析每一行的数据
    date, stock_code, price_str, volume_str = line.split(',')
    price = float(price_str)
    volume = int(volume_str)
    # 更新统计数据
    total_volume += volume
    highest_price = max(highest_price, price)
    lowest_price = min(lowest_price, price)
    # 记录每个股票的总成交量
    if stock_code in price_dict:
        price_dict[stock_code]['volume'] += volume
    else:
        price_dict[stock_code] = {'volume': volume}
# 打印统计结果
print(f"Total Volume: {total_volume}")
print(f"Highest Price: {highest_price:.2f}")
print(f"Lowest Price: {lowest_price:.2f}")


# In[20]:


#ch3-7
sum = 0
for i in range(1, 100+1):
    sum = sum +i
print("sum=", sum)


# In[22]:


#ch3-8
sum_odd = 0
sum_even = 0
for i in range(1, 100+1):
    if i%2 ==1:
        sum_odd = sum_odd + i
    else:
        sum_even = sum_even + i
print("1~100中所有的奇数和：", sum_odd)
print("1~100中所有的偶数和：", sum_even)


# In[23]:


#ch3-9
n = int(input("请输入一个正整数："))
for i in range(1, n+1):
    if n%i ==0:
        print(i, end = ' ')


# In[1]:


#ch3-10
sum = 0
i = 1
while i<=100:
    sum = sum + i 
    i = i +1
print("sum=", sum)


# In[3]:


x = float (input("请输入一个实数："))
y = 1.0
while y * y != x:
    y = (y + x/y)/2
print("算术平方根为：", y)


# In[7]:


#ch3-11
import math
x = float (input("请输入一个实数："))
n = 0
y = 1.0
while abs(x -y * y) > 1e-8:
    y = (y + x/y)/2
    n = n + 1
    print(n, y)
print("算术平方根为：", y)
print("sqrt函数求出的算术平方根为：", math.sqrt(x))


# In[12]:


for s in "Python":
    if s == "t":
        continue
    print(s, end="")


# In[13]:


for s in "Python":
    if s == "t":
        break
    print(s, end="")


# In[14]:


#ch3-12
m = int(input("输入一个正整数 m: "))
n = int(input("输入一个正整数 n: "))
for i in range(min(n,m), 0, -1):
    if m % i ==0 and n % i ==0:
        print("{}和{}的最大公约数为：{}".format(m, n, i))
        break


# In[15]:


for s in "Python":
    if s =="t":
        continue
    print(s, end= "")
else:
    print("正常退出")


# In[16]:


for s in "Python":
    if s =="t":
        break
    print(s, end= "")
else:
    print("正常退出")


# In[17]:


#ch3-13 定义矩形的行数和列数
rows = 5
columns = 10

# 外层循环控制行
for i in range(rows):
    # 内层循环控制列
    for j in range(columns):
        # 打印星号
        print("*", end=" ")
    # 每打印完一行后换行
    print()


# In[18]:


#ch3-14 赌场“幸运7”游戏模拟
from random import * 
money = 10
max = money

while money >0:
    num1 = randint(1,6)
    num2 = randint(1,6)
    if num1 + num2 == 7:
        money += 4
        if money > max: max = money
    else: 
        money -= 1
    print(money, end = ' ')
print('\nmax=', max)


# In[20]:


group1 = ["萧峰", 98]
group2 = ["杨过", 96]
groups = [group1, group2]
print(groups)


# In[ ]:




