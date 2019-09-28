# Python编程快速上手
让繁琐工作自动化

## 从Web抓取信息

`bs4`的`select`方法返回的是一个element的list

## 处理Excel电子表格

1. openpyxl.load_workbook('XXX')需要在当前工作目录才能处理。可以导入os，使用函数os.getcwd()弄清楚当前的工作目录，并使用os.chdir()改变当前工作目录