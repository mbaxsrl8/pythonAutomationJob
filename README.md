# Python编程快速上手
让繁琐工作自动化

## 从Web抓取信息

`bs4`的`select`方法返回的是一个element的list

## 处理Excel电子表格

1. openpyxl.load_workbook('XXX')需要在当前工作目录才能处理。可以导入os，使用函数os.getcwd()弄清楚当前的工作目录，并使用os.chdir()改变当前工作目录

## 处理CSV文件

1. 并非CSV文件中的每个逗号，都表示两个单元格之间的分界。CSV文件也有自己的转义字符，允许逗号和其他字符作为值的一部分。`split()`方法不能处理这些转义字符。因为这些潜在的缺陷，所以总是应该用csv模块来读写CSV文件。

2. 遇到文件编码错误，应该在打开文件的时候指定编码，如：

   ```python
   exampleFile = open('example.csv', encoding='utf-8')
   ```

   

3. 对于大型的csv文件，需要在一个for循环中使用Reader对象，这样避免将整个文件一次性装入内存。