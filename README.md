# Python_Notes
This is my Python learning notes.

一、数字

	1.检测字符串是不是负数：str.lstrip('-').isdigit()
	2.二进制字符串'101'转十进制：int(str,2)
二、字符串

	1.字符串的排序
	    1）字符串的就地反向：s[:] = s[: : -1]，s[:]表示数组中所有子模块
	2.列表转字符串
	    1）"".join(str(each)  for each in list)
	3.字符串的常用操作
	    1）字符串的拼接："".join([ str(x)   for x in y   if x ])
	    2）字符串的拆分：str.split()
	    3）字符串的居中：str.center(width, 'fillchar')
	    4）字符串输出小细节：print('Today is:  ' + str(today))，即冒号：后面有个小空格
	    5）字符串和数字直接的相互转换：ord('a') = 97   chr(97) = a
	    6）字符串中每个字符个数的统计：collections.Count(str)
	    7）字符串转数字：int(str)
	4.字符串格式化
	    1）f' hello {name}'
	5.原始字符串输出：r''this is a line with \n'' ，可以让反斜杠不发生转义
	6.字符串的性质：
	    1）字符串和元组一样，一旦确定下来就不能对其进行修改。只能通过创建一个新的字符串，通过切片和拼接来实现更新
	7.子字符串
三、列表

	1.列表的排序
	    1）list.sort()
	    2）sorted(list)
	2.字符串转列表
	    1）list.append(obj)
	    2）list(string)
	3.列表的常用操作：
	    1）嵌套列表的遍历：for x, y, z  in list
	    2）enumerate()函数将一个可遍历的数据对象组合成一个索引序列：for i, element in enumerate(seq)
	    3）列表表达式：[ x for x in list if x ]
	    4）将两个列表的元素组成一个列表表达式：[(x,y) for x in [1,2] for y in [2,3] if x!=y]
	    5）嵌套列表表达式：[[row[i] for row in mat] for i in range(3)]
	    6）定义一个初始化嵌套列表：mat = [[0] * m for _ in range(n)]
	4.列表的复制
	    1）不能用=，这样两个列表就是同一个列表
	    2）要用list.copy()，这还只是浅拷贝
	    3）深拷贝要用copy.deepcopy(list)
	5.列表的赋值
	    1）等长的列表可以用 = 直接对应位置赋值
	    2）for循环一个一个的赋值
	6.列表的表头插值
	    1）list.insert(0, obj)
	7.列表的扩展
	    1）list.extend(seq)
四、元组

	1.元组与列表的区别
	    1）元组只可读，不可写；对于 元组，逗号才是关键，小括号只是起到补充的作用
	    2）元组中的元素不可修改，但并不妨碍我们创建一个新的元组，即利用切片和拼接实现更新元组的目的，同名的元组的id不同，并不是同一个对象
五、字典

	1.字典的排序
	    1）sorted()对字典的键从小到大排序
	    2）sorted(dict.values())对字典的值从小到大排序
	    3）sorted(dict.items(),key=lambda x:x[1])返回元组组成的列表，其中x[0]是键，x[1]是值
	    4）字典列表的排序：sorted(dict,key=lambda x:x[key])按照字典key对应的值进行从小到大排序
	    5）有序字典：collections.OrderedDict()
	    6）sorted(dict1.items(), key = lambda x:(x[1], x[0])) 对字典的值从小到大排序，然后对值相同的按键从小到大排序
	2.列表转字典
	    1）两个列表转字典：dict(zip(list1,list2))，zip()函数创建的是一个只能访问一次的迭代器
	    2）二级列表只有两个元素的嵌套列表转字典：dict(list)
	    3）元组列表转字典：dict(list)
	    4）简单列表转字典：dict(enumerate(list))，索引为键
	    5）字典列表转字典：dict.updata()
	3.字典的合并
	    1）c = {**a, **b}    **-unpacking(解包)
	4.字典表达式
	    1）{x:x**2 for x in （2，4，6）}
	    2）{x:x**2 for x in range(2，8，2）}
	5.多值映射字典
	    1）              
		
	6.有序字典
	    1）可以使用collections模块中的OrderedDict类
	7.两个字典的集合操作
	    1）a.keys() & b.keys()，valus()不支持集合操作，因为不能保证所有的值互不相同
	    2）a.items() & b.items()
	    3）排除指定几个键：
		
六、集合

	1.集合的性质
	    1）set()创造的集合内部是无序的
	    2）集合类似于列表，只是同样的元素只能出现一次，即集合不能包含重复的元素
	2.列表转集合
	    1）方法：set(list)
	    2）作用：将直接删除其中多余重复的元素，使得留下来的元素不重复  
七、类

	1.类的定义：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象共有的属性和方法。对象是类的实例
	2.self代表类的实例，代表当前对象的地址，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
八、收集器

    1.Countrer.most_common(3)：出现频率最高的3个数据
    2.Counter的实例之间可以进行集合操作
    3.itertools.groupby()函数可以对数据进行分组
九、基础语法

	1.C和Java都是尽可能让商更大，而Python则是尽可能让商更小
	2.Python的加减法运算符优先级高于左移右移运算符，而Java相反
	3.一个数和相同的异或偶数次，结果不变即可以用来求奇数次的数字
	4.Python程序中的名字（变量、参数、函数名等）关联着作为其值的对象，变量的这种实现方式称为变量的引用语义，在变量里保存值的引用
	5.变量的值语义：把变量的值直接保存在变量的存储区
	6.and逻辑操作符加到while循环中可以控制循环的次数
	7.pass是个占位语句，表示它不做任何事情
	8.星号*在形参中的作用是打包，而在实参中的作用是解包
	9.在函数内部可以访问全局变量，但是无法修改全局变量的值，除非使用global关键字来实现
	10.可以使用lambda关键字来定义匿名函数
	11.字典的键必须不可变，所以可以用数值、字符串或元组充当，如果使用列表那就不行
	12.有别于序列，字典是不支持拼接和重复（*n）操作
	13.#后面要加一个空格再写注释内容
	14.Python input()函数返回为字符串类型
	15.shell：命令行解释器
	16.JSON(JS对象简谱)：一种轻量级数据交换格式
	17.yield的作用是把一个函数变成一个generator，调用函数并不会执行函数，而是返回一个iterable对象
	18.负数在计算机中是以补码的形式存储的
	19.在一个类的定义中，由下划线_开头的属性名（和函数名）都当作内部使用的名字，不应该在这个类之外使用
	20.类相当于模具，用于批量生产对象
	21.类的继承：class 类名(父类名)
	22.多态：不同对象对同一方法响应不同的行动
	23.self就是实例对象
	24.私有变量：变量名前加双下划线，可以通过实例对象._类名__对象名来访问私有对象
十、标准输入输出

	1.从键盘读入一行：sys.stdin.readline().strip('\n')
	2.将读入的列表字符串转为列表：eval(str)；eval() 函数用来执行一个字符串表达式，并返回表达式的值
	3.牛客网刷题输入输出：
		n = int(input())
		data = []
		for _ in range(n):
			s = input()
			if s != '':
				tmp = [each for each in s.split()]
				data.append(tmp)
			else:
				break
		print(data)
		
		data = []
		while True:
			s = input()
			data.append(list(map(str, input().split(''))))
		print(data)
