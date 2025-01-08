#!/usr/bin/env python
# coding: utf-8

# # 第四章 列表与数组

# In[5]:


group1 = ["林冲", 98]
group2 = ["关胜", 97]
groups = [group1, group2]
print(groups) # [['林冲', 98], ['关胜', 96]]


# In[6]:


names = ["林冲", "关胜","董平","呼延灼","秦明"]
print(names[4])# 秦明
print(names[-1]) # 秦明


# In[7]:


# 例4-1 根据输入的数字，输出对应的月份信息
monthes=["January","February","March","April","May","June","July","August","September","October","November","December"]
m=int(input("请输入整数月份"))
print("It's {}.".format(monthes[m-1]))


# In[11]:


lst1 =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst1.append("武松") #  ["林冲", "关胜","董平","呼延灼","秦明"]
lst1.insert(0,"卢俊义") # ['卢俊义', '林冲', '关胜', '董平', '呼延灼', '秦明', '武松']
lst1.extend(["鲁智深"]) # ['卢俊义', '林冲', '关胜', '董平', '呼延灼', '秦明', '武松', '鲁智深']
lst2 = ["花荣"] 
lst3 = lst1 + lst2 # ['卢俊义', '林冲', '关胜', '董平', '呼延灼', '秦明', '武松', '鲁智深', '花荣']
print(lst3)


# In[21]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst.remove("林冲") #['关胜', '董平', '呼延灼', '秦明']
removed_element = lst.pop(0) #  ['董平', '呼延灼', '秦明']
del lst[1] # ['董平', '秦明']
del lst 


# In[23]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
del lst
#print(lst) # 引发NameError, name 'lst' is not defined


# In[25]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst[4] = "武松" # ['林冲', '关胜', '董平', '呼延灼', '武松']
print(lst)


# In[27]:


empty_list = []
lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
print("两个列表的长度分别为{}和{}".format(len(empty_list), len(lst)))


# In[28]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明","林冲"]
lst.count("林冲") # 输出2


# In[29]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
print("林冲" in lst)
print("林冲" not in lst)


# In[31]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst.index("关胜") # 输出1


# In[6]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
for i in range(5):
    print("{} 是水泊梁山五虎将之一".format(lst[i]))


# In[1]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
for item in lst:
    print(item)


# In[10]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
for index, value in enumerate(lst):
    print("Index:{},Value:{}".format(index, value))

for index, value in enumerate(lst,2):
    print("Index:{},Value:{}".format(index, value)) #输出整个列表的元素


# In[11]:


#ch4-1 
suspects=['A','B','C','D']
for x in suspects:
    if (x!='A') + (x=='C') + (x=='D') + (x!='D')==3:
        print("\n小偷是:",x)
        break


# In[25]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst[:5] # 输出['林冲', '关胜', '董平', '呼延灼', '秦明']
lst[3:] # 输出['呼延灼', '秦明']
lst[-1:1:-2] #输出 ['秦明', '董平']
lst[::-1] #输出 ['秦明', '呼延灼', '董平', '关胜', '林冲']


# In[27]:


hereos1 = ["林冲", "关胜","董平","呼延灼","秦明"]
hereos2 = ["宋江", "吴用","公孙胜"]
hereos1 + hereos2 # 输出 ['林冲', '关胜', '董平', '呼延灼', '秦明', '宋江', '吴用', '公孙胜']


# In[30]:


hereos1 = ["林冲", "关胜","董平","呼延灼","秦明"]
hereos2 = ["宋江", "吴用","公孙胜"]
hereos2.extend(hereos1)
hereos2 #输出 ['宋江', '吴用', '公孙胜', '林冲', '关胜', '董平', '呼延灼', '秦明']


# In[31]:


hereos2 = ["宋江", "吴用","公孙胜"]
hereos2 * 3 # 输出 ['宋江', '吴用', '公孙胜', '宋江', '吴用', '公孙胜', '宋江', '吴用', '公孙胜']


# In[34]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst_copy = lst
lst_copy # 输出 ['林冲', '关胜', '董平', '呼延灼', '秦明']


# In[35]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst_copy = lst[:]
lst_copy # 输出 ['林冲', '关胜', '董平', '呼延灼', '秦明']


# In[36]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst_copy = lst.copy()
lst_copy


# In[42]:


original_list = [1, 2, 3, [4, 5]]
copied_list = original_list.copy()
copied_list[0] = 3 # 列表修改
copied_list[3].append(6) #列表修改
print(copied_list)  # 输出: [3, 2, 3, [4, 5, 6]]
print(original_list) # 输出: [1, 2, 3, [4, 5, 6]]


# In[46]:


import copy

# 创建一个包含可变对象的原始列表
original_list = [1, 2, 3, [4, 5]]

shallow_copied_list = copy.copy(original_list) # 使用浅拷贝
shallow_copied_list[3].append(6) # 修改浅拷贝中的可变对象
print("Shallow copied list:", shallow_copied_list)  # 输出: [1, 2, 3, [4, 5, 6]]
print("Original list:", original_list) # 输出: [1, 2, 3, [4, 5, 6]]，原始列表也被修改

deep_copied_list = copy.deepcopy(original_list) # 使用深拷贝
deep_copied_list[3].append(7) # 修改深拷贝中的可变对象
print("Deep copied list:", deep_copied_list) # 输出: [1, 2, 3, [4, 5, 7]]
print("Original list:", original_list) # 输出: [1, 2, 3, [4, 5, 6]]，原始列表没有被修改


# In[2]:


lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
lst.clear()
type(lst) # 输出 list的类型


# In[8]:


person = "John", "Doe", "male", "25"  #使用逗号将元素隔离开来生成元组
print(person) # 输出 ('John', 'Doe', 'male', '25')
person1 = ("Micheal", "Johnson", "male", "29")  #使用逗号将元素隔离开来生成元组
print(person1) # 输出 ('Micheal', 'Johnson', 'male', '29')


# In[9]:


single_element_typle = (24,)  # 创建一个包含单个元素的元组需要在元素后面加上逗号
person =("John", "Doe", "male", "25")
first_name, last_name, gender, age = person
print(first_name, last_name, gender, age) # 输出：John, Doe, male, 25


# In[4]:


person = “John”, “Doe”, “male”, “25”  # 使用逗号将元素隔离开来生成元组
print(person) # 输出：(‘John’, ‘Doe’, ‘male’, ’25’)
color = (“red”, “blue”, “yellow”, person)  # 一个元组可以作为另一个元组的元素，在不混淆语义的情况下圆括号不是必须的
print(color) # 输出：(‘red’, ’blue’, ’yellow’, (‘John’, ‘Doe’, ‘male’, ’25’)) 
print(color[2]) # 输出：‘blue’
print(color[-1][2])  # 可以采用多级索引获取信息，输出：‘male’
single_element_typle = (24,)  # 创建一个包含单个元素的元组需要在元素后面加上逗号，否则会被视为括号运算符而非元组
first_name, last_name, gender, age = person
print(first_name, last_name, gender, age)
# 输出：John, Doe, male, 25


# In[11]:


group1 = ("林冲", "豹子头",98)
group1[1] # 输出 '豹子头'


# In[16]:


group1 = [("林冲", "豹子头",98), ("秦明", "霹雳火",96),("董平", "双枪将",95)]
group1[0] # 输出 ('林冲', '豹子头', 98)
group1[0][1] #输出 '豹子头'


# In[19]:


group1 = [("林冲", "豹子头",98), ("秦明", "霹雳火",96),("董平", "双枪将",95)]
group1[0] = ("林冲", "豹子头",97) # 结果 [('林冲', '豹子头', 97), ('秦明', '霹雳火', 96), ('董平', '双枪将', 95)]
group1[0][2]= 97 # TypeError: 'tuple' object does not support item assignment


# In[23]:


group1 = ("林冲", "豹子头",98)
lstgroup1 = list(group1) #将元组转换成列表 ['林冲', '豹子头', 98]
lst =  ["林冲", "关胜","董平","呼延灼","秦明"]
group1lst = tuple(lst) # 将列表转换成元组('林冲', '关胜', '董平', '呼延灼', '秦明')


# In[26]:


my_string = "Hello World!"
my_list = list(my_string) # 结果是['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']


# In[29]:


my_string = "Hello World!"
my_list = my_string.split()
print(my_list) # 输出 ['Hello', 'World!']
my_string1 =  "林冲,关胜,董平,呼延灼,秦明"
my_list1 = my_string1.split(',')
print(my_list1) # 输出 ['林冲', '关胜', '董平', '呼延灼', '秦明']


# In[30]:


my_string = "hello"
my_list = [char for char in my_string]
print(my_list)  # 输出：['h', 'e', 'l', 'l', 'o']


# In[33]:


my_string = "hello world！"
my_list = [char for char in my_string if char != " " and char !="!"]
print(my_list)  # 输出：['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']


# In[34]:


lstnum = input("请输入一个数值列表：\n") #输入 [1,2,3,4,5,6,7]
print(lstnum) # 输出  [1,2,3,4,5,6,7]
type(lstnum) # 输出类型 str


# In[35]:


lstnum = eval(input("请输入一个数值列表：\n")) #输入 [1,2,3,4,5,6,7]
print(lstnum) # 输出  [1, 2, 3, 4, 5, 6, 7]
type(lstnum) # 输出类型 list


# In[39]:


lstnum = list(range(1,8))
print(lstnum) # 输出 [1, 2, 3, 4, 5, 6, 7]
type(lstnum) # list


# In[44]:


lst = [["林冲", "豹子头",98], ["秦明", "霹雳火",96],["董平", "双枪将",95]]
valuesofforce = [item[2] for item in lst if item[2] >= 96]
print(valuesofforce) # 输出 [98, 96]


# In[45]:


lnum = [i**2 for i in range(1, 11)]
print(lnum)


# In[52]:


#ch4-2  输入10个学生的成绩，求最高分、最低分和平均分
scores = eval(input("请输入10个学生的分数列表:\n"))
maxscore = max(scores)
minscore = min(scores)
avescore = sum(scores)/len(scores)
print("这次考试的最高分是{},最低分是{},平均分是{}。\n".
      format(maxscore, minscore, avescore))


# In[ ]:




