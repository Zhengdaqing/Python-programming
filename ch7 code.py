#!/usr/bin/env python
# coding: utf-8

# In[8]:


#ch7-1 
import csv

with open('example.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
print('Hellow world!')        


# In[7]:


import csv

# 待写入的数据列表
data = [
    ['国家', '2019年GDP(亿美元)', '2019年人均GDP(美元)'],
    ['美国', 21433226, 65112],
    ['中国', 14342903, 10261],
    ['日本', 5081770, 40259]]

# 打开CSV文件
with open('example.csv', 'w', newline='', encoding = 'gbk') as csvfile:
    csv_writer = csv.writer(csvfile)
    # 写入数据
    for row in data:
        csv_writer.writerow(row)
        
with open('example.csv', 'r', newline='', encoding= 'gbk') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


# In[ ]:


with open ("vCard.json", "r+") as f:
    f.read(10)
    f.tell()
    f.read()
    f.tell()
    


# In[ ]:




