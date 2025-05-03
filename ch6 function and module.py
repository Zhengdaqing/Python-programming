#!/usr/bin/env python
# coding: utf-8

# # 第六章 函数与模块

# print函数及其参数的用法

# In[9]:


# print输出一个或多个对象
print("李逵",["李逵","宋江"],{"宋江":"及时雨"})
# sep参数设置输出对象间隔
print("李逵","宋江","吴用",sep="|")
# end参数设置输出结尾符
for ele in ['李逵','宋江','吴用']:
    print(ele,end=',')
# file参数设置写入对象
with open("./test.txt","w+") as f:
    print("宋江的外号是及时雨",file=f)
with open("./test.txt","r+") as f:
    print(f.read())
# flush参数设置输出缓存流
# 这是实现的是一个逐个延迟输出效果(打字机效果)
import time
for char in "宋江的外号是及时雨":
    print(char,flush=True,end="")
    time.sleep(1)


# input函数及其参数的用法

# In[10]:


# 不带提示信息的input函数用法
user_input = input()
print("你输入的内容是：",user_input)
# 带提示信息的input函数用法
hero_name = input("请输入宋江的外号:")
print("宋江的外号是",hero_name)


# len函数及其参数的用法

# In[11]:


# len函数获取字符串长度
hero_name = "宋江"
print(hero_name,"的名字长度为：", len(hero_name))
# len函数获取列表长度
heroes = ["宋江", "吴用", "公孙胜", "卢俊义"]
print("梁山好汉列表长度为：", len(heroes))


# range函数及其参数的用法

# In[12]:


liangshan_heroes_top10 = [
    "宋江","卢俊义","吴用","公孙胜","关胜",
    "林冲","秦明","呼延灼","花荣","柴进"
]
# 最基本的range用法，生成从0到4的整数序列
for i in range(5):
    print(liangshan_heroes_top10[i], end=' ')
print()  # 换行
# 指定start和stop参数，生成从3到5的整数序列
for i in range(3,6):
    print(liangshan_heroes_top10[i], end=' ')
print()  # 换行
# 指定start、stop和step参数，生成从2开始，每次加2，直到小于10的整数序列
for i in range(2, 10, 2):
    print(liangshan_heroes_top10[i], end=' ')


# format函数及其参数的用法

# In[13]:


# 基本用法，使用位置参数替换占位符
hero_name = "宋江"
hero_nickname = "及时雨"
formatted_string = "梁山好汉{}，外号{}".format(hero_name, hero_nickname)
print(formatted_string)
# 使用关键字参数替换占位符，参数顺序可以任意
formatted_string_with_kwargs = "梁山好汉{name}，外号{nickname}".format(name=hero_name, nickname=hero_nickname)
print(formatted_string_with_kwargs)
# 使用位置参数和关键字参数混合替换占位符
hero_rank = 1
formatted_mixed = "梁山好汉排名第{rank}位：{name}，外号{nickname}".format(rank=hero_rank, name=hero_name, nickname=hero_nickname)
print(formatted_mixed)
# 使用索引来访问位置参数，适用于占位符较多的情况
heroes = ["宋江", "卢俊义", "吴用"]
formatted_with_index = "梁山好汉前三位分别是：{0}，{1}和{2}".format(*heroes)
print(formatted_with_index)
# 格式化数字，如控制浮点数的小数位数、整数的格式等
hero_age = 45.6789
formatted_number = "宋江的年龄约为{:.2f}岁".format(hero_age)
print(formatted_number)
# 综合模拟输出梁山好汉信息
print("梁山好汉信息：")
hero_info = "名字：{name:>4}，外号：{nickname:^8}，排名：{rank:0>3}，年龄：{age:.1f}岁"
print(hero_info.format(name="宋江", nickname="及时雨", rank=1, age=45.7))


# In[15]:


hero_name = "宋江"
hero_nickname = "及时雨"
hero_rank = 1
hero_age = 45.67
# format函数格式化
hero_info = "名字：{name:>4}，外号：{nickname:^8}，排名：{rank:0>3}，年龄：{age:.1f}岁"
print(hero_info.format(name=hero_name, nickname=hero_nickname, rank=hero_rank, age=hero_age))
# f-string格式化
print(f"名字：{hero_name:>4}，外号：{hero_nickname:^8}，排名：{hero_rank:0>3}，年龄：{hero_age:.1f}岁")


# sorted函数及其参数的用法

# In[1]:


# 基本用法，对列表进行升序排序
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("升序排序后的列表：", sorted_numbers)
# 使用 key 参数，根据字符串长度对列表进行排序
words = ["apple", "key", "cherry", "date"]
sorted_words_by_length = sorted(words, key=len)
print("按长度升序排序后的字符串列表：", sorted_words_by_length)
# 使用 reverse 参数，对列表进行降序排序
sorted_numbers_desc = sorted(numbers, reverse=True)
print("降序排序后的列表：", sorted_numbers_desc)
# 使用lambda函数自定义排序规则，例如根据好汉的年龄排序
heroes = [("宋江", 45), ("卢俊义", 38), ("吴用", 50)]
sorted_heroes_by_age = sorted(heroes, key=lambda x: x[1])
print("按年龄升序排序后的梁山好汉列表：", sorted_heroes_by_age)


# open函数及其参数的用法

# In[2]:


file_path = './test.txt'
# 写入模式，创建或覆盖文件
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("梁山好汉排名\n")
    file.write("宋江\n")
    file.write("卢俊义\n")
# 读取模式，读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("文件内容：")
    print(content)
# 追加模式，在文件末尾追加内容
with open(file_path, 'a', encoding='utf-8') as file:
    file.write("吴用\n")
# 再次读取文件，查看追加后的内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.readlines()
    print("追加后的文件内容（逐行读取）：")
    for line in content:
        print(line, end='')  # end='' 去掉默认的换行符，因为 line 本身已经包含换行


# type 和 isinstance 函数的用法

# In[4]:


# 使用 type 函数获取对象的类型
hero_name = "吴用"
hero_name_type = type(hero_name)
print("hero_name的类型：", hero_name_type)
# 使用 isinstance 函数检查对象类型
is_name_str = isinstance(hero_name, str)
print("hero_name 是否是 str 类型：", is_name_str) 
# 检查自定义类的实例,这里类的语法无需掌握
class Hero:
    def __init__(self,name):
        pass
song_jiang = Hero("宋江")
# 使用 type 检查
hero_type = type(song_jiang)
print("song_jiang 的类型：", hero_type)
# 使用 isinstance 检查
is_song_jiang_hero = isinstance(song_jiang, Hero)
print("song_jiang 是否是 Hero 类的实例：", is_song_jiang_hero)  # 输出: True


# 特殊功能函数的具体用法

# In[10]:


heroes_top5 = [
    "宋江","卢俊义","吴用","公孙胜","关胜"
]
hero_nickname = [
    '及时雨', '玉麒麟', '智多星', '入云龙', '大刀'
]
# 使用enumberate遍历列表，同时索引与元素
for idx,element in enumerate(heroes_top5):
    print(f"排名{idx+1}的好汉是{element}")
# 使用zip函数组合名称与外号列表,返回名称-外号映射字典
hero_nickname_map = dict(zip(heroes_top5,hero_nickname))
print(hero_nickname_map)
# 使用map函数映射各个好汉的外号
print("前五的好汉的外号为:",list(map(lambda x:hero_nickname_map[x],heroes_top5)))
# ord返回字符对应的ASCII码值
print("A的ASCII码值为:",ord('A'))
# chr返回ASCII码值对应的字符
print("ASCII码为65对应的字符为:",chr(65))


# 常见数学函数的具体用法

# In[12]:


# sum函数返回求和
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"{numbers} 的总和是 {total}")
# max返回最大值
max_value = max(numbers)
print(f"{numbers} 中的最大值是 {max_value}")
multiple_max = max(3, 7, 2, 8)
print(f"多个参数中的最大值是 {multiple_max}")
# min返回最小值
min_value = min(numbers)
print(f"{numbers} 中的最小值是 {min_value}")
multiple_min = min(3, 7, 2, 8)
print(f"多个参数中的最小值是 {multiple_min}")
# abs返回绝对值
absolute_value = abs(-10)
print(f"-10 的绝对值是 {absolute_value}")
# power返回x的y次幂
result_power = pow(2, 0.5)
print(f"2 的 0.5 次幂是 {result_power}")
# divmod返回两个数相除的商和余数
quotient, remainder = divmod(10, 3)
print(f"10 除以 3 的商是 {quotient}, 余数是 {remainder}")
# round返回四舍五入的结果
rounded_value = round(3.14159, 2)
print(f"3.14159 四舍五入到小数点后2位是 {rounded_value}")


# # 课后习题

# 习题1

# In[ ]:


import math

def calculate_circle_area(radius):
    # 待补充内容
    pass

# 测试
radius = 5
area = calculate_circle_area(radius)
print(f"半径为 {radius} 的圆的面积是 {area}")


# 习题2

# In[ ]:


def find_max_min(numbers):
    # 待补充内容
    pass

# 测试
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_value, min_value = find_max_min(numbers)
print(f"列表中的最大值是 {max_value}，最小值是 {min_value}")


# 习题3

# In[ ]:


def format_student_info(name, age, grade):
    # 待补充内容
    pass

# 测试
name = "张三"
age = 20
grade = "大三"
info = format_student_info(name, age, grade)
print(info)


# 习题4

# In[ ]:


def count_word_frequency(file_path):
    # 待补充内容
    pass

# 测试
file_path = 'test.txt'  # 假设 test.txt 是存在且包含文本内容的文件
freq = count_word_frequency(file_path)
for word, count in freq.items():
    print(f"{word}: {count}")


# 习题5

# In[ ]:


def contains_palindrome(lst):
    # 待补充内容
    pass

# 测试
lst = ['a', 'b', 'c', 'b', 'a']
result = contains_palindrome(lst)
print(f"列表中是否存在回文子串：{result}")

