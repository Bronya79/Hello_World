f = open('.\\python\\文件与数据库\\ex1.txt', mode='w', encoding='utf-8')

print(f.name)
print(f.mode)
print(f.closed)
f.write('www.runoob.com')
f.close()
