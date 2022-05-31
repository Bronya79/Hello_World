from tkinter import W


with open('.\\python\\文件与数据库\\ex1.txt', 'r', encoding='utf-8') as f:
#    f.write('Hello')
    print(f.read)
    for line in f:
        print(line.strip())
