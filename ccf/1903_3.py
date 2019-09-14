import binascii
x = '14151617'
y = bytearray.fromhex(x)
print(y)
print(hex(eval('00')))
print(str(hex(eval('0x14151617')^eval('0xB4B5B6B7'))).lstrip('0x').upper())
print('###############开始################')
n,s,l = map(int,input().split(' '))# 阵列数目 条带大小(块) 硬盘大小
print(n,s,l)# 如果 s=1 需要取8个字符

"""
0 000102030405060710111213141516172021222324252627
1 000102030405060710111213141516172021222324252627
"""
# 输入，两个字符表示一个字节硬盘的内容
strings = []
ans =[] # 存放块的结果
long = [0]*l
for j in range(l):
    string = input().split(' ')[1]
    strings.append(string)
for j in range(len(strings)):
    temp = []
    while long[j] != len(strings[j]):
        temp.append(strings[j][long[j]:long[j]+8])
        long[j] += 8
    ans.append(temp)
print(ans)
# 两种可能  第一种 n == l
block = []
long = [0]*l
i = 0
while 1:
    now = 0
    while now < s :
        block.append(ans[i][long[i]])
        long[i]+=1
        now += 1
    # 如果到了最后一个列表的 最后一个字符串 结束
    if i == len(ans)-1:
        if long[i] != len(ans[len(ans) - 1]):
            i = 0
        else:
            break
    else:
        i += 1
print(block)
# 两种可能  第二种 n != l
if n == l:
    block = ans[0]


# 输入要查找的块的个数
num = int(input())
block_num = []
for i in range(num):
    block_num.append(int(input()))
    # 从已有词典中输出要查找块中的十六进制数
for i in range(len(block_num)):
    print(block[i])