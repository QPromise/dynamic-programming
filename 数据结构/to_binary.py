"""
题目：计算一个十进制数对应的二进制数中1的个数
"""
####################################
count = 0
num = 10
while num:
    count += num & 0x01
    num = num >> 1
    print(num)
print('位运算计1的个数:',count)
####################################
num = 10
ans = []
count = 0
while num:
    count += 1 if num % 2 == 1 else 0
    ans.insert(0,num%2)
    num //= 2
print('复杂度为logn:',count)
#####################################
"""
去掉无关的0，从右往左，统计1的个数
"""
count = 0
num = 10
while num:
    num &= (num-1)
    count += 1
print('复杂度只与1的个数有关:',count)
"""
二分查找
"""
array = [1,5,9,11,22,33,41,52,68,94,203,333,541,654]
mid = len(array)
begin = 0
tail = len(array)
num = int(input('请输入待查找的数字：\n'))
while begin < tail:
    mid=(begin + tail)//2
    if num == array[mid]:
        print('已找到',mid)
        break
    elif num > array[mid]:
        begin = mid
    else:
        tail = mid
if begin > tail:
    print('not found')