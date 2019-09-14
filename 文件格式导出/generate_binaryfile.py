def gen_binaryfile(filename,size,quantity = 1):
    for q in range(quantity):
        #首先以路径path新建一个文件，并设置模式为写
        file = open(filename+str(q)+'.bin','wb')
        #根据文件大小，偏移文件读取位置
        file.seek(1024*1024*size)#姑且以MB为单位吧
        #然后在当前位置写入任何内容，必须要写入，不然文件不会那么大哦
        file.write(bytes(1))
        file.close()
gen_binaryfile('bin_test',800)

