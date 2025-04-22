#数据容器的切片操作[起始:终止:步长]都为下标，取的元素是起始下标——终止下标-1

"""
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[0:10:])

my_tuple = (1,2,3,4,5,6,7,8,9)
print(my_tuple[0:10:2])

my_str = '0123456789'
print(my_str[::2])
print(my_str[::-1]) #将序列反转，反向输出
print(my_str[9:0:-1])

#练习

my_str = '学大海河,来就,学大上'
print(my_str[::-1])
print(my_str[::-1].split(',')[2])
"""
"""
#4.  set 集合 无序的，不能用下标访问,每次打印都是乱序  允许修改  会去除重复元素
my_set = {"name","year","height","year"}
void_set = set()
print(void_set)
print(my_set)


# 添加元素 .add
my_set.add("money")
my_set.add("name")
print(my_set)

#移除元素 .remove
my_set.remove("year")
print(my_set)
    # ,pop 取出一个随机元素，集合里面去掉这个元素
my_set.pop()
print(my_set)

#清空集合  .clear
my_set.clear()
print(my_set)
"""

"""
#取两个集合的差集
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,4}
c = a.difference(b)   #取a中有b中没有的形成新集合c，集合a b元素不变
print(c)
print(a)
print(b)

#消除两个集合的差集
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,4}
a.difference_update(b) #删除a中和b相同的元素，a会变，b不变
print(a)
print(b)

#两个集合合并
c = a.union(b)  #一个新集合，相同元素去重
print(c)

#len（）求长度
print(len(c))

#集合的遍历 不能用while 因为无法使用下标
i = None
for i in b:
    print(i)


#集合训练 信息去重

my_list = [1,2,3,3,5,6,4,5,1,4,2,5,1,1]
my_set = set()
for i in my_list:
    my_set.add(i)

print(my_set)
"""

#5.字典 dict()   {key:value}  key值不能重复  value可以重复  无下标索引  但能通过key访问到对应的value值
            #如果key重复 取最后一个key：value                        return dict[kay] = value
void_dict = dict()  #或者 void_dict = {}
print(void_dict)
my_dict = {"name":"55","lahua":"54","wangwang":"325"}
print(my_dict)
print(my_dict["name"])

#嵌套字典
stu_score_dict = {
    "李华":{
        "数学":52,
        "语文":65,
        "英语":85
    }, "张强":{
        "数学":99,
        "语文":85,
        "英语":75,
    }
}
print(stu_score_dict)
print(stu_score_dict["张强"]["语文"])


#字典常用操作
#增加或更新元素
stu_score_dict["张超"]=dict()
stu_score_dict["张超"]["数学"]=52
stu_score_dict["张超"]["语文"]=52
stu_score_dict["张超"]["英语"]=52
print(stu_score_dict)
print(stu_score_dict["张超"])

stu_score_dict["张超"]["英语"]=99
print(stu_score_dict["张超"])

#.pop  取出value值并删除kay
a = stu_score_dict.pop("李华")
print(a)
print(stu_score_dict)

#.clear 清空字典

#.keys  获取全部key
print(stu_score_dict.keys())

#for循环遍历字典
i = None
for i in stu_score_dict.keys():
    print(f"名字是{i}")
    print(f"分数是{stu_score_dict[i]}")

#或者  for i in  stu_score_dict

#字典练习
