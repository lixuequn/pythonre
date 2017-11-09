# encoding: UTF-8
#!/usr/bin/python

import os
import sys

# info=os.getcwd()
# listfile=os.listdir(os.getcwd())
info = raw_input("请输入要列举文件的目录：(如D:\\temp)")
listfile = os.listdir(info)
filename = open(info + 'file.txt', 'w')
print listfile
# out=open(listfile,'r')

for line in listfile:  # 把目录下的文件都赋值给line这个参数
    print line  # 打印出赋值的内容
    # filename.write(filename)
    if line[-3:] == '.py' or line[-4:] == '.txt':

        print line
        out = open(line, 'r')  # 定义读取line里面的内容，也就是读取每个文件的内容
        for com in out:  # 把每个文件的内容（也就是目录下的文件）赋值给com
            filename.write(line + ":  " + com)

    else:
        print (line + '  ' + "该文件是目录形式")
filename.close()
