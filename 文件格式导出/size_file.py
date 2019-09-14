import os
import random
import struct
def genSizeFile(fileName, fileSize):
    #file path
    filePath=fileName+".bin"

    # 生成固定大小的文件
    # date size
    ds=0
    with open(filePath, "wb") as f:
        while ds<fileSize:
            f.write(bytes(random.randint(0,255)))
            ds=os.path.getsize(filePath)
            print(os.path.getsize(filePath))

# start here.
genSizeFile("binary_test",10000*1024)