# coding=utf-8
"""
1.列表-list
    可以用来存储内容可变 长度可变 类型可以不同 有序的数据
    的数据结构。类似于java的list


"""
# 定义列表
list1 = [1,2,3,True,False,'physics','w']
# 访问列表
print(list1[1])
print(list1[3:6])   # 取出第4-6个的元素
print(list1[:4])
print(list1[2:])
print(list1[-2])    # physics,倒着数第二个
# 更新列表
list1[4] = "x"
print(list1)
# 删除元素
del list1[3:6]
# 拼接
print([1,2,3] + ["a","b","c"])
# 重复三次
print([1,2,3]*3)
"""
    列表其他的api
    cmp(x1,x2)比较两个列表元素
    len(list) 列表元素个数
    max(list) 返回列表元素最大值
    min(list）返回列表元素最小值
    list(seq) 将元祖转换为列表
    list.append(obj) 在列表末尾添加新的对象
    list.count(obj) 统计某个元素在列表中出现的次数
    list.insert(index,obj)将对象插入列表
    list.pop（obj=list[-1])移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
    list.remove(obj) 移除列表中某个值的第一个匹配项
    list.reverse() 反向列表中的元素
    list.sort([func])对原列表进行排序
元组 tuple
    不能修改的列表
"""
# 定义元祖
t1 = (1,"aa",19,"bj","2010",123.23)
print(t1[1])
print(t1[2:4])
print(t1[2:])
print(t1[:4])
print(t1[-2])
# 修改元祖 - 元组不能修改，但是可以将多个元祖拼接为一个新元祖
t1 = (1,"aaa",19)+(2,"bbb",20)
print(t1)

# 删除整个元祖 - 元组元素不可删除 但是可以删除整个元祖
t = (1,"aaa",19,"bj",222.22)
del t
print(None)
"""
    元祖其他函数
    cmp(t1,t2)比较元祖
    len(t) 计算元祖个数
    max
    min
    tuple(seq)
set
    集合，不可重复，不可修改，且无序的列表
    Set的基本用法
"""
# Set
# 定义Set
s = {"aa",123,"bb","aa"}
print(s)

# 访问set
for i in s:
    print(i)
"""
4.dict 字典
    存储键值对类型的数据
    键不可重复 无序
    类似于java中的Map
    dict的基本用法
"""
# dict
d = {"name" : "zs","age" : 18}
print(d['name'])
# 修改
d['name'] = 11
# 删除字典
del d["age"]
d.clear()
del d
# print(d)
"""
1.定义函数
通过def关键字定义函数，之后跟函数名称和小括号包裹的参数列表，之后跟
一个冒号，在其后编写函数体。
函数体的第一行内容，可以直接是一个字符串，此字符串不影响函数体的内容，相当于
是该方法的文档声明，用来描述函数的给你，可以后续查看

def functionname(parameters):
    "文档字符串"
    函数体
通过return关键字在函数内部返回，可以选择行返回一个返回值，如果return
后没有明确返回值，则默认返回一个None
"""
def fun(a):
    " hello,world "
    print(a)
fun(1)
"""
2.函数的调用
    通过函数名之后跟小括号传入参数值就可以调用函数了
    函数调用过程中，也可以在实参列表中明确的指定实参要赋值给哪一个
    实参列表的顺序可以和形参列表不同
3.缺省参数
    在定义函数过程中，可以全部或者部分函数参数指定默认值，则在调用函数的
    过程中可以选择性的不传入这些参数，则这些参数采用默认值执行参数
"""
def sumx2(n1,n2=10):
    return n1+n2
print(sumx2(2,3))
print(sumx2(2))
"""
4.不定长参数
    类似于java中的可变参数,python中的参数也可以具有不定长的参数，未来再
    入0个或多个实参，而在函数的内部可以按照使用数组的形式使用该不定长参数
    一个函数中，不定长参数最多只能有一个，且必须出现在函数参数列表的最后一位
    可以通过在形参前加*实现不定长
"""
# 不定长
def sumx(*nums):
    sum = 0
    for n in nums:
        print(n)
sumx(1,2,3,4)
"""
5.函数直接量定义函数
    通过lambda表达式来声明一个函数，lambda关键字之后跟参数列表，再跟冒号
    之后函数的体，这种方式声明的函数函数体只能是一个表达式，如果函数体有多条语句
    则无法通过此方式定义函数
"""
sumx5 = lambda n1,n2:n1+n2
"""
6.函数是一等公民
    在python中函数一等公民，具有完整的能力，属性能做的函数都可以做。
        a.作为类的成员
        b.作为局部成员
        c.高阶函数作为方法参数
        d.高阶函数作为方法返回值
"""
# 函数作为类的成员
class Person:
    name = ""
    age = 0
    def eat(self,food):
        print("吃"+food)
    def sleep(self):
        print("睡...")
def eat(food):
    def cook(food):
        return "做熟"+food
    print("吃"+cook(food))
p = Person
p.eat
# 高阶函数 将函数作为方法的参数传递
def eatx(food,how2Cook):
    foods = how2Cook(food)
    print(foods)
def cookYRC(food):
    return "烤熟"+food
eatx("字符串",cookYRC)

# 高阶函数 可以将函数作为另一个函数的返回值返回

def lookUpCaipu(cai):
    if cai == "羊肉串":
        def cookYRC(food):
            return "烤熟"+food
        return cookYRC
    elif cai == "涮羊肉":
        return lambda food:"做熟"+food
    else:
        return lambda food:"做熟"+food
cookFunc = lookUpCaipu("涮羊肉")
print(cookFunc("羊肉"))
