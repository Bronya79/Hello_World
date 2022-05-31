# R

## R基本运算

## R基础语法

- print()
- cat()  
cat() 函数支持直接输出结果到文件：

```r
cat("RUNOOB", file="/Users/runoob/runoob-test/r_test.txt")
```

## R数据类型

最基本三种数据类型

1. 数字
2. 逻辑  
3. 文本  

数字计数法则：

- 一般型
- 科学计数法

逻辑类型在许多其他编程语言中常称为布尔型（Boolean），常量值只有 TRUE 和 FALSE。  

最直观的数据类型就是文本类型。文本就是其它语言中常出现的字符串（String）

有关于 R 语言的变量定义，并不像一些强类型语言中的语法规则，需要专门为变量设置名称和数据类型，每当在 R 中使用赋值运算符时，实际上就是定义了一个新的变量.

按对象类型来分是以下 6 种：

- 向量（vector）
- 列表（list）
- 矩阵（matrix）
- 数组（array）
- 因子（factor)
- 数据框（data.frame)

向量从数据结构上看就是一个线性表，可以看成一个数组。
c() 用于创建一个新的向量

```R
a = c(3, 4)
b = c(5, 0)
a + b
[1] 8 4
>
```

## 1、向量

## 2、列表

## 3、R矩阵

M行(row) * N列(colunm)
R语言可以用matrix()函数来创建矩阵

```R
matrix(date=NA, nrow=1, ncol=1, byrow=FALSE, dimnames=NULL)
```

- 参数说明  
    - date
    - nrow
    - ncol
    - byrow
    - dimname

### 转置矩阵

```r
t()
```

### 矩阵计算

- 矩阵加减法
- 矩阵乘除法

## 4、数组

R语言创建数组使用array()函数，该函数用向量作为参数，可以使用dim设置数组维度。

- 参数说明
    - data 向量，数组元素
    - dim 数组的维度，默认是一维数组
    - dimnames 维度的名称，必须是个列表，默认情况下不设置

```r
vector1 <- c(5, 9, 3)
vector2 <- c(10, 11, 12, 13, 14, 15)
cloumn.names <- c("COL1", "COL2", "COL3")
row.names <- c("ROW1", "ROW2", "ROW3")
matrix.names <- c("Matrix1", "Matrix2")
result <- array(c(vector1, vector2), dim = c(3, 3, 2), dimnames = list(row.names, cloumn.names, matrix.names))
print(result)
```

### 访问数组元素

列索引和行索引

```r
vector1 <- c(5, 9, 3)
vector2 <- c(10, 11, 12, 13, 14, 15)
cloumn.names <- c("COL1", "COL2", "COL3")
row.names <- c("ROW1", "ROW2", "ROW3")
matrix.names <- c("Matrix1", "Matrix2")
result <- array(c(vector1, vector2), dim = c(3, 3, 2), dimnames = list(row.names, cloumn.names, matrix.names))
print(result[3,,2])
print(result[1,3,1])
print(result[,,2])
```

### 操作数组元素

通过访问矩阵元素来访问数组元素
apply()函数计算数组中两个矩阵中每一行对数字之和

## 5、因子（待补充）

创建因子使用factor()函数

```r
factor(x = character(), levels, labels = levels, exclude = NA, ordered = is.ordered(x), nmax = NA)
```

- 参数说明：
    - x：向量。
    - levels：指定各水平值, 不指定时由x的不同值来求得。
    - labels：水平的标签, 不指定时用各水平值的对应字符串。
    - exclude：排除的字符。
    - ordered：逻辑值，用于指定水平是否有序。
    - nmax：水平的上限数量。

## 6、 数据框（待补充）

数据框是 R 语言的数据结构，是特殊的二维列表。  
数据框每一列都有一个唯一的列名，长度都是相等的，同一列的数据类型需要一致，不同列的数据类型可以不一样  

```R
data.frame(…, row.names = NULL, check.rows = FALSE, check.names = TRUE, fix.empty.names = TRUE, stringsAsFactors = default.stringsAsFactors())
```

- …: 列向量，可以是任何类型（字符型、数值型、逻辑型），一般以 tag = value 的形式表示，也可以是 value。
- row.names: 行名，默认为 NULL，可以设置为单个数字、字符串或字符串和数字的向量。
- check.rows: 检测行的名称和长度是否一致。
- check.names: 检测数据框的变量名是否合法。
- fix.empty.names: 设置未命名的参数是否自动设置名字。
- stringsAsFactors: 布尔值，字符是否转换为因子，factory-fresh 的默认值是 TRUE，可以通过设置选项（stringsAsFactors=FALSE）来修改。

例：

```R
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
   
)
```
数据框的数据结构可以通过 str() 函数来展示：
```R
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
)
# 获取数据结构
str(table)
```
输出结果为：、
```
'data.frame':   2 obs. of  3 variables:
 $ 姓名: chr  "张三" "李四"
 $ 工号: chr  "001" "002"
 $ 月薪: num  1000 2000
```
summary() 可以显示数据框的概要信息：
```R
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
   
)
# 显示概要
print(summary(table))
```
输出结果为：
```
姓名               工号                月薪     
Length:2           Length:2           Min.   :1000  
Class :character   Class :character   1st Qu.:1250  
Mode  :character   Mode  :character   Median :1500  
                                      Mean   :1500  
                                      3rd Qu.:1750  
                                      Max.   :2000  
```

我们也可以提取指定的列：

```R
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
)
# 提取指定的列
result <- data.frame(table$姓名,table$月薪)
print(result)
```

输出结果为：

```R
table.姓名 table.月薪
1       张三       1000
2       李四       2000
```

## 数据重塑

## R包

## csv文件

### CSV 表格交互

CSV（Comma-Separated Values，CSV，有时也称为字符分隔值，因为分隔字符也可以不是逗号） 是一种非常流行的表格存储文件格式，这种格式适合储存中型或小型数据规模的数据。  
由于大多数软件支持这个文件格式，所以常用于数据的储存与交互。  
CSV 本质是文本，它的文件格式极度简单：数据一行一行的用文本保存起来而已，每条记录被分隔符分隔为字段，每条记录都有同样的字段序列。

CSV 用逗号来分割列，如果数据中含有逗号，就要用双引号将整个数据块包括起来。  
注意：包含非英文字符的文本要注意保存的编码，由于很多计算机普遍使用 UTF-8 编码，所以我是用 UTF-8 进行保存的。  
注意： CSV 文件最后一行需要保留一个空行，不然执行程序会有警告信息。

例如：

```csv
id,name,url,likes
1,Google,www.google.com,111
2,Runoob,www.runoob.com,222
3,Taobao,www.taobao.com,333

```

### 读取csv文件

使用read.csv()函数

```R
data <- read.csv("sites.csv", encoding="UTF-8")
print(data)
```

read.csv()返回的是数据框

使用方法：、

```R
data <- read.csv("sites.csv", encoding="UTF-8")
print(is.data.frame(data))  # 查看是否是数据框
print(ncol(data))  # 列数
print(nrow(data))  # 行数
```

以下统计数据框中 likes 字段最大对数据

```R
data <- read.csv("sites.csv", encoding="UTF-8")
# likes 最大的数据
like <- max(data$likes)
print(like)
```

我们也可以指定查找条件，类似 SQL where 子句一样查询数据，需要用到到函数是 subset()。

以下实例查找 likes 为 222 到数据：

```R
data <- read.csv("sites.csv", encoding="UTF-8")=
# likes 为 222 的数据
retval <- subset(data, likes == 222)
print(retval)
```

注意：条件语句等于使用 ==  
多个条件使用 & 分隔符，以下实例查找 likes 大于 1 name 为 Runoob 的数据：

```R
data <- read.csv("sites.csv", encoding="UTF-8")
# likes 大于 1 name 为 Runoob 的数据
retval <- subset(data, likes > 1 & name=="Runoob")
print(retval)
```

### 保存为csv文件

R 语言可以使用 write.csv() 函数将数据保存为 CSV 文件。
接着以上实例，我们将 likes 为 222 的数据 保存到 runoob.csv 文件：

```R
data <- read.csv("sites.csv", encoding="UTF-8")
# likes 为 222 的数据
retval <- subset(data, likes == 222)
# 写入新的文件
write.csv(retval,"runoob.csv")
newdata <- read.csv("runoob.csv")
print(newdata)
```

X 来自数据集 newper，可以通过参数 row.names = FALSE 来删除它

```R
data <- read.csv("sites.csv", encoding="UTF-8")
# likes 为 222 的数据
retval <- subset(data, likes == 222)
# 写入新的文件
write.csv(retval,"runoob.csv", row.names = FALSE)
newdata <- read.csv("runoob.csv")
print(newdata)
```
