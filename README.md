# dp
## 简介:
dp.py是通过用户指定规则提交随机的输入，自行运行两个程序并比对结果，以用于python代码快速检查错误的对拍程序，对于ccf，python语言的考试很有帮助
## 用法:
### 1. 准备工作
将待检错、用于提交的python程序和时间空间复杂度高、用于检错的python程序放在同一个目录中，检错程序的命名为:（原程序名称+"p"，不考虑后缀名.py)

将dp.py也放在这个目录中，运行dp.py
### 2. 输入内容
#### 2.1 定值输入
先看一个简单的例子:
![201312-2简单例子](https://s2.ax1x.com/2019/03/18/Amn2es.png)
在这道题目中，我们可以看到其输入内容仅为一个字符串:0-670-82162-4

分析:1行，1个字符串，为固定值“0-670-82162-4”

则在dp输入的时候，输入"1 \"0-670-82162-4\"\n\n"就可以 （注:为突出回车符等符号，避免与本文其他内容混淆，以后输出都以字符串的形式表示）

其中1代表本类输入仅输入一行，""代表字符串，这样本行输入参数就只有字串0-670-82162-4。之后再利用最后\n的空行结束输入。

但是我们一般更常见的是这种数字的输入
![201503-3例子](https://s2.ax1x.com/2019/03/18/AmKQgO.png)

这种转换为dp输入，便是"1 5 2 7 2014 2015\n\n"。

对于数字，不需要双引号，当然你也可以输入"1 \"5\" \"2\" \"7\" \"2014\" \"2015\"\n\n"
#### 2.2 r()实现随机动态输入
当然，定值输入对大量数据调试并没有多大改进（因为人也能做定值输入），自然有必要让机器自动生成满足条件的输入样例。

这里介绍r()函数:随机数生成器，r(n)代表1到n-1内的整数，r(m,n)代表m到n-1内的整数

还看刚才的两个例子，现在我想在所有满足条件的输入中随机生成输入。

对于例1,我们输入"1 \"r(0,10)-r(0,10)r(0,10)r(0,10)-r(0,10)r(0,10)r(0,10)r(0,10)r(0,10)-r(0,10)\"\n\n"（待优化）

当然这里还缺少尾数为X的情况，可以在测试后把最后一个r(0,10)改成"X"再测试

例2相对容易一些，"1 r(13) r(5) r(8) r(1850,1950) r(1950,2050)\n\n"

后面两个年份这么设置是为了保证其有序性。
#### 2.3 c\[\]\[\]实现取参数
上面的例2，如果想试验所有的年份，由于第二个年份须大于第一个年份，在生成第二个年份的时候就要取第一个年份的值才能满足需求。

"1 r(13) r(5) r(8) r(1850,2050) ...

此时r(1850,2050)位于第一行，第四个位置（1是行数，不考虑），故应该用c\[0\]\[3\]去取r(1850,2050)的这个值

dp输入为:"1 r(13) r(5) r(8) r(1850,2050) r(c\[0\]\[3\],2051)"
#### 2.4 ge实现的行重复参数以及行首数实现的列重复参数
行重复语法:数字串ge非空格字符串，相当于“非空格字符串 非空格字符串 ... 非空格字符串”，个数为数字的值
![例3](https://s2.ax1x.com/2019/03/18/Am8IsK.png)

这种输入的题目不少，那如果要调试的话怎么办呢？

使用"1 r(1000)\nc\[0\]\[0\]ger(10000)\n\n"

我们再看一下每行开头参数不是1的情况:
![例4](https://s2.ax1x.com/2019/03/18/AmJwuV.png)
dp输入:"1 r(10) r(10)\nc\[0\]\[0\] r(0,4) r(0,4) r(c\[1\]\[0\],6) r(c\[2\]\[0\],6)\nc\[1\]\[0\] r(6) r(6)\n\n"
### 3 效果
dp.py随机生成99个输入样例，对每一个样例匹配，每匹配成功一个，输出一个".",若匹配失败，输出Error，输入参数以及两程序各自的输出参数。
