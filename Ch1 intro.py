#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
a1 = np.array([1, 2, 6, 4, 1])


# In[ ]:


a1.argmax


# 分段函数:|
# $
# sign(x)=\geginl{cases}
# 1, &x>0 \\0, &x=0 \cr -1, &x<0
# \end{cases}
# $

# In[3]:


# 使用dir()函数获取一个对象中的所有属性和方法，包括内置函数
print(dir(__builtins__))


# In[11]:


import math

radius = 100
area = math.pi * radius **2
print(area)

st = "I am a teacher of SUFE."
print(st)


# In[9]:


print(y)


# In[2]:


# 用解包赋值实现两个变量的值交换
a = 1
b = 2
print(a,b)
a, b = b, a
print(a,b)


# In[3]:


def compound_interest(principle, rate, time):
    amount = principle * (1+ rate) ** time
    return round(amount, 2)
#input parameters
principle = float(input("请输入本金："))
rate = float(input("请输入年利率（采用小数形式）："))
time = int(input("请输入投资年限："))

final_amount = compound_interest(principle, rate, time)
print(final_amount)


# In[ ]:




