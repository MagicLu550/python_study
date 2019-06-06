import math
# coding=utf-8
"""
a.编码
    python2默认使用iso8859-1，python3默认使用utf-8
    如果python文件本身的编码和以上编码不一致会出现乱码问题
    此时可以在文件中通过如上注释通知解释器解析当前文件时候采用的编码，两
    码一致可以解决乱码
    #coding utf-8
b.语句
    Python通常一行为一条语句，不需要分号标识
    如果将多条语句写在一行内，则需要使用分号分割防止发生歧义
c.缩进
    python中没有使用大括号作为作用域的标识，而是采用制表符来标识
    而是采用制表符来标识作用范围

"""

print("hello,python~")
if 3>2:
    print("aaa")
    if 5>4:
        print("bbb")
    print("ccc")
print("ddd")

"""

由于python使用制表符作为作用范围标识，所以制表符不能随意使用，之前通过的制表符
来调整代码结构的习惯需要改变

d.注释：

    python使用#作为单行注释 使用三个单引号 或 三个双引号


"""

# 单行注释

"""
多行注释
"""

"""

python的注释 python也常使用注释作为文档的特性声明，例如向解释器声明当前页面的编码

e. 引用
    python没有声明引用的关键字，直接写引用的名称就是在声明一个引用
    python的引用没有数据类型的区别，也即一个引用可以先后指向不同类型的数据
    python中小写的引用表示一个变量 大写引用表示一个常量，此处的常量本质上
    还是变量，此处的常量只是一种约定，要求未来使用这不要进行修改，如果真的修改
    也是成功的
"""
x = 10
x = 100
x = "abc"
PI = 3.14
PI = 3.1415

"""
2.标识符

    标识符标准和java基本一样,Python的下划线是有特殊意义
        以单下划线开头_foo的代表不能直接访问的类属性，需通过类提供的接口进行访问
        不能用from xxx import *而导入
        
        以双下划线开头__foo代表类的私有成员
        
        以双下滑线开头和结尾的__foo__代表Python里特殊方法专用标识，如__init__代表
        类的构造方法
3.数据类型
    python中的引用是没有数据类型，但是数据本身是有类型区别的
    a.字符串类型
        可以用单引号 双引号 三引号 来声明字符串
        三引号声明的字符串中可以包含任意字符 这些字符会被直接当作字符串的内容 从而
        省去转义的过程
"""
str = 'abc'
str = "def"
str = '''
hello lop ss[
aaa sdd
    ghi
'''

"""
python中可以使用r或R在字符串直接量前修饰，表明当前字符串直接转义，忽略原数值
python的字符串提供了大量的操作方法
1) +拼接字符串
2) *重复字符串
3) []索引字符串
4) in
5) not in
6) %
"""
str = "abc"+"def"
print("abc"*3)
print(str[2])       # c 定位第3个
print(str[2:4])     # cd 截取为第3个和第4个，不包含尾部
print(str[:4])      # abcd 截取前4个(保留定位以前，不保留定位)
print(str[2:])      # cdef 截取后4个(保留定位及定位以后)

str = "abcdefg"
print("xyz" in str)  # 判断是否包含
print("xyz" not in str)  # 判断不包含

#格式化字符串
str = "My name is park,age us 18,my city is bj"
str = "My name is tlp,age us 18,my city is mg"
str = "My name is swk,age us 18,my city is hgs"

str = "My name ia %s,my age is %d,my city us %s" % ("park",18, "beijing")
print(str)


# r和R的用法
str = "abc \r\n ndef"
print(str)
str = "abc \\r\\n ndef"
print(str)
str = r"abc \r\n ndef"

"""    
    b.布尔类型
    布尔类型直接量只有两个值：
     True False
    使用逻辑操作符操作布尔类型的数据
"""

flag = True
flag = False
flag = True and False
flag = True or False

"""
    可以使用逻辑操作符号
    c.数值类型
    python中代表数据的类型。可以有如下四种直接量的值：
    整形
        通常称为是整形或整数，是正或负整数，不带小数点
    长整型
        无限大小的整数，整数最后是一个大写或小写的l
    浮点型
        浮点型由整数部分和小数部分组成，浮点型也可以通过科学技术法表示
    复数
        复数由实数部分和虚数部分构成，可以用a+bj，或者
        complex(a,b)表示，复数的实部a和虚部b都是浮点型
    提供了一些数学函数
"""
n = abs(-10)
print(n)
n = max(1,2,3,4,7,5,4)
print(n)
print(math.pi)
print(math.e)
"""            
    d.空值
    类似于java的null，表示没有值，只有一个直接量
    None
4.运算符
    a.  关系运算符
        == 等于 比较对象是否相等
        != 不等于 比较两个对象不等 
        <> 不等于
        < 大于
        > 小于
        >=大于等于
        <=小于等于
    b. 赋值运算符 
        =简单的赋值运算符
         
"""
x = None




