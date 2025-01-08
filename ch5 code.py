#!/usr/bin/env python
# coding: utf-8

# # 第五章 字典和集合

# In[2]:


# 使用列表结构模拟字典
words = ['apple','banana','potato']
meanings = ['苹果','香蕉','土豆']
# 假如你想要查找apple的释义
# 用列表的实现方式如下
meanings[words.index('apple')] # 输出 '苹果'


# ## 字典创建与常见操作

# 字典的创建

# In[2]:


# 创建空字典
empty_dict = {}
print(empty_dict)
# 手动创建键值对
translate_dict = {"apple":"苹果","banana":"香蕉","potato":"土豆"}
print(translate_dict)


# In[3]:


# 使用关键字参数创建字典
person_info = dict(name="Alice", age=30, city="New York")
print(person_info)
 # 使用映射对象（二元组列表）创建字典
mapping = [("apple", "苹果"), ("banana", "香蕉"), ("cherry", "樱桃")]
fruit_dict = dict(mapping)
print(fruit_dict)


# In[4]:


# 生成一个数字到其平方的字典
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)
# 生成一个偶数到其平方的字典（只包含1到10内的偶数）
even_squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares_dict)


# 字典的访问

# In[5]:


# 创建一个示例字典
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# 直接访问字典中的值
alice_score = student_scores["Alice"]
print(f"Alice's score: {alice_score}")

# 使用get方法访问字典中的值
bob_score = student_scores.get("Bob")
print(f"Bob's score: {bob_score}")

# 使用get方法访问不存在的键，返回None或指定的默认值
david_score = student_scores.get("David",0)  # David不存在，返回默认值0
print(f"David's score (default): {david_score}")

# 使用setdefault方法访问字典中的值，键不存在时设置默认值
# Charlie存在，返回其原有的值
charlie_score = student_scores.setdefault("Charlie",0)
print(f"Charlie's score: {charlie_score}")

# 使用setdefault方法访问不存在的键，设置并返回默认值
eva_score = student_scores.setdefault("Eva",90)  # Eva不存在，设置默认值90
print(f"Eva's score (set default): {eva_score}")

# 查看更新后的字典
print(f"Updated student scores: {student_scores}")


# In[6]:


# 创建一个示例字典
fruit_dict = {"apple": "苹果", "banana": "香蕉", "orange": "橙子"}

# 检查键 "apple" 是否在字典中
is_apple_in_dict = "apple" in fruit_dict
print(is_apple_in_dict)

# 检查键 "grape" 是否在字典中
is_grape_in_dict = "grape" in fruit_dict
print(is_grape_in_dict)


# 字典的删除

# In[7]:


# 创建一个示例字典
example_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
# 使用 del 删除指定键的元素
del example_dict['apple']
print(example_dict)
# 使用 pop 方法删除指定键的元素，并返回其值
banana_value = example_dict.pop('banana')
print(banana_value)  
print(example_dict)  
# 使用 pop 方法删除指定键的元素，并设置默认值
banana_value = example_dict.pop('banana',None)
print(banana_value) 
# 使用 popitem 方法删除随机项
last_item = example_dict.popitem()
print(last_item)  
print(example_dict) 


# 字典的遍历

# In[8]:


# 创建一个示例字典
example_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 键(keys)遍历
for key in example_dict.keys():
    print(f"Key: {key}")

# 值(values)遍历
for value in example_dict.values():
    print(f"Value: {value}")

# 键值对(items)遍历
for key, value in example_dict.items():
    print(f"Key: {key}, Value: {value}")


# 字典的整体操作

# In[9]:


# 创建一个包含一些键值对的字典
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
# 使用 clear 方法清空字典
my_dict.clear()
print(my_dict)


# In[10]:


# 创建一个包含一些键值对的字典
original_dict = {"name": "Alice", "age": 30, "hobbies": ["reading", "swimming"]}
print("Original dictionary:", original_dict)
# 使用 copy 方法创建字典的浅拷贝
copied_dict = original_dict.copy()
print("Copied dictionary:", copied_dict)
# 修改原字典中的不可变对象
original_dict["age"] = 18
# 修改原字典中的可变对象
original_dict["hobbies"].append("cooking")
print("Modified original dictionary:", original_dict)
print("Copied dictionary after modifying original:", copied_dict)


# In[11]:


# 创建一个包含一些键值对的字典
original_dict = {"name": "Alice", "age": 30}
print("Original dictionary:", original_dict)
# 创建一个新的字典，用于更新原字典
update_dict = {"age": 35, "city": "New York"}
# 使用 update 方法更新原字典
original_dict.update(update_dict)
print("Updated dictionary:", original_dict)


# ## 集合创建与常见操作

# 集合的创建

# In[12]:


# 这里需要注意的是{}不代表空集合,代表的空字典
fake_set = {}
print("the actual type of fake_set is",type(fake_set))
# 手动创建一个集合
my_set = {1, 2, 3, 4, 5}
print("Manually created set:", my_set)
# 尝试创建包含重复元素的集合，重复元素会被自动去除
another_set = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicate elements:", another_set)


# In[13]:


# 使用set创建空集合
empty_set = set()
print("empty_set:",empty_set,',type:',type(empty_set))
# 使用 set 函数将列表转换为集合
my_list = [1, 2, 2, 3, 4, 4, 5]
converted_set = set(my_list)
print("Set created from list:", converted_set)
# 使用 set 函数将字符串转换为集合（字符串会被视为字符的序列）
my_string = "hello"
string_set = set(my_string)
print("Set created from string:", string_set)


# 集合的常见操作

# In[14]:


# 创建一个空集合
my_set = set()
print("Initial set:", my_set)
# 使用 add 方法向集合中添加元素
my_set.add(1)
print("Set after adding 1:", my_set)
# 尝试添加已存在的元素，集合不会改变
my_set.add(1)
print("Set after attempting to add 1 again:", my_set)


# In[15]:


# 创建一个包含一些元素的集合
my_set = {1, 2, 3, 4}
print("Initial set:", my_set)

# 使用 remove 方法移除元素
my_set.remove(3)
print("Set after removing 3:", my_set)
# 尝试移除不存在的元素，会引发报错
# my_set.remove(5)  # 这行代码会引发错误

# 使用 discard 方法移除元素
my_set.discard(2)
print("Set after discarding 2:", my_set)
# 尝试丢弃不存在的元素，不会引发错误
my_set.discard(5)
print("Set after attempting to discard 5:", my_set)


# 集合的数学运算

# In[16]:


# 创建两个集合
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {4,5}
# 使用 issubset 方法判断 set_a 是否是 set_b 的子集
print(set_a.issubset(set_b))
# 使用 <= 运算符判断
print(set_a <= set_b)
# 使用 issuperset 方法判断 set_b 是否是 set_a 的超集
print(set_b.issuperset(set_a))
# 使用 >= 运算符判断
print(set_b >= set_a)
# 使用isdisjoint判断 set_a 是否与 set_c 不相交
print(set_a.isdisjoint(set_c))


# In[17]:


# 创建两个集合
set_c = {1, 2, 3}
set_d = {2, 3, 4}
# 使用 intersection 方法或 & 运算符获取交集
print(set_c.intersection(set_d),set_c & set_d)
# 使用 union 方法或 | 运算符获取并集
print(set_c.union(set_d),set_c | set_d)
# 使用 difference 方法或 - 运算符获取差集
print(set_c.difference(set_d),set_c - set_d)
# 使用 symmetric_difference 方法或 ^ 运算符获取对称差集
print(set_c.symmetric_difference(set_d),set_c ^ set_d)


# # 实例代码

# ## 使用字典模拟JSON复杂查询

# **背景介绍：** JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，它易于人阅读和编写，同时也易于机器解析和生成。它采用完全独立于语言的文本格式，这些特性使JSON成为理想的数据交换语言，广泛应用于网络数据传输，API开发、配置文件设置与日志记录等，是目前运用的十分广泛的数据传输语言。

# **问题描述：** JSON数据由键值对组成，每个键值对之间用逗号分隔，这与Python中的字典十分相似，现在要求使用字典模拟JSON的数据格式，实现JSON复杂嵌套查询，要求输入查询链，返回对应的查询结果，比如输入name->first_name，返回John。

# **代码思路：** 这个问题实际上考察的字典的嵌套查询，我们首先需要运用字符串的相关方法对输入的查询链进行拆解，再根据查询链中的键的顺序逐个嵌套查询，同时考虑到用户误输入的可能性，我们也应该使用更加安全的get方法进行查询，具体代码如下：

# In[19]:


# 示例字典（模拟JSON）
JSON_data = {
    "name": {
        "first_name": "John",
        "last_name": "Doe"
    },
    "age": 30,
    "address": {
        "city": "New York",
        "detail":{
            "street":"Wall Street",
            "number":"100"
        },
        "zipcode": "10001"
    },
    "hobby":["writing","reading","jogging"]
}

# 输入部分
# 输入查询链
query_chain = input("请输出JSON查询链:")
# 分割查询链为键列表
key_list = query_chain.split("->")

# 查询部分
# 初始化当前层级为最外层数据字典
current_level = JSON_data
# 逐层遍历键列表
for key in key_list:
    # 进入下一层级,使用安全的get方法查询
    current_level = current_level.get(key,None)
    # 如果查询结果不存在或输入错误
    if current_level is None:
        print("查询结果不存在或输入错误!")
        break
else:
    # 正常结束查询,输出查询结果
    print("查询结果为:",current_level)


# ## 使用Python统计词频

# **背景介绍：** 词频统计是一种文本分析方法，用于计算和分析在一段文本中各个词汇出现的频率，可以为后续的深入自然语言处理（NLP）提供基础性分析，其广泛应用于文本主题识别、信息检索与词云图绘制当中。

# **问题描述：** 现有一个已经分词以及预处理后的单词列表，现在要求使用字典统计单词列表中各个单词的词频，并按词频的大小降序输出。

# **代码思路：** 这个问题实际上考察的字典的访问与排序，我们首先需要逐个遍历单词列表并分别在字典中相应单词词频中加1，值得注意的是，还没统计到的单词为在字典中出现，因此我们使用更加安全的get方法设置默认值来统计，具体代码如下：

# In[20]:


# 假设已经分词并预处理后的单词列表
word_list = [
    "apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "kiwi", "banana","apple"
]

# 统计词频阶段
# 初始化一个空字典来存储词频
word_freq = {}
# 遍历单词列表，统计词频
for word in word_list:
    # 使用get方法在单词还没统计时,设置词频为0,避免报错
    word_freq[word] = word_freq.get(word,0)+1

# 将词频字典按值（词频）降序排序,并输出
# 首先，将字典项转换为列表，列表中的元素为 (frequency, word) 元组
word_freq_list = [(value,key) for key,value in word_freq.items()]
# 将列表降序排序,列表元素为元组,符合元组首位元素比较法则
word_freq_list.sort(reverse=True)
# 输出排序后的词频列表
for freq,word in word_freq_list:
    print(word,":",freq)


# ## 使用Python解决集合论问题

# **背景介绍：** 集合论是数学的一个基本分支，它研究的是对象（称为元素）的集合以及这些集合之间的关系和运算。集合具有无序性、互异性和确定性三大特性，这些特性使得集合成为数学和计算机科学中处理数据的基本工具。集合论在数据库设计、算法分析、逻辑推理等领域有着广泛的应用。

# **问题描述：** 选课是大学中的常见情景，现在有两门选修课A与B，各自有选课的同学名单，现在教务处想要统计如下内容，请在Python中编程实现：1.同时选A与B课程的学生人数
# 2.选修课程A与B的学生总人 
# 3.仅选修课程A的学生总 4.数
# 仅选修一门课程的学生总人数

# **代码思路：** 这个问题实际上考察的是Python中集合的基本运算，我们可以根据一定的数学知识将该问题建模为集合论问题，并使用Python中提供的集合常见数学运算求解，具体代码如下：

# In[1]:


# 定义选课学生集合
course_A = {"Alice", "Bob", "Charlie", "David"}
course_B = {"Bob", "David", "Eve", "Frank"}

# 1. 同时选A与B课程的学生人数
both_courses = course_A & course_B  # 交集运算
num_both_courses = len(both_courses)
print("同时选A与B课程的学生人数:",num_both_courses)

# 2. 选修课程A与B的学生总人数
all_students = course_A | course_B  # 并集运算
num_all_students = len(all_students)
print("选修课程A与B的学生总人数:",num_all_students)

# 3. 仅选修课程A的学生总人数
only_course_A = course_A - course_B  # 差集运算
num_only_course_A = len(only_course_A)
print("仅选修课程A的学生总人数:",num_only_course_A)

# 4. 仅选修一门课程的学生总人数
only_one_course = course_A ^ course_B  # 对称差集运算
num_only_one_course = len(only_one_course)
print("仅选修一门课程的学生总人数:",num_only_one_course)


# # 课后习题

# 习题1

# In[ ]:


# 针对字典dict_test = {"ab": 5, "cd": 7, "ef": 3}，思考以下操作
dict_test = {"ab": 5, "cd": 7, "ef": 3}
# 1. len(dict_test)的结果是多少？

# 2. 如何向字典中添加键值对""gh": 8"

# 3. 如何修改"ab"对应的值为1

# 4. 如何删除"ef"对应的键值对？


# 习题2

# In[ ]:


# 根据课程A和课程B的学生名单表，使用集的概念，找到同时在两个班的学生名单
classA = ["Bob", "Alice", "David", "Catherine", "Gauss", "Euler", "Kate"]
classB = ["Catherine", "Rose", "Hopper", "Keith", "Bob"]


# 习题3

# In[ ]:


# 创建两个集合，分别包含几个整数
setA = {1,2,3}
setB = {2,4,5}
# 然后展示两个集合的交集、并集、差集


# 习题4

# In[ ]:


# 编写一个程序，提示用户输入一系列用空格分开的数字，然后创建一个集合以去除重复项，并打印出最终的结果


# 习题5

# In[ ]:


# 5.已知一个购物车里有以下商品及对应数量：{"apple": 3, "banana": 6, "cherry": 2}。
# 编写一个程序，让用户输入商品名称和购买数量，如果商品存在于购物车中，则更新数量。如果商品不存在，则添加商品及其数量。

