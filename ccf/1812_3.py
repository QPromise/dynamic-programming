# print(bin(int(hex(5),16)))
# num_bin = str(bin(int(hex(17),16))).split('b')[1]
# num_bin = '0'*(8-len(num_bin)) + num_bin
# print(num_bin)
def count_len(string):
    nums = [int(i) for i in string.split('.')]
    num_bins = []
    for num in nums:
        num_bin = str(bin(int(hex(num), 16))).split('b')[1]
        num_bin = '0' * (8 - len(num_bin)) + num_bin
        #print(num,num_bin)
        num_bins.insert(0, num_bin) # 字符串逆置
    real_length = 0
    omit_length = 0
    for i, num_bin in enumerate(num_bins):
        # print(i, num_bin)
        rsum_0 = 7 - num_bin.rfind('1')
        # 精确 or 省略长度
        if rsum_0 != 8:
            real_length += rsum_0
            break
        else:
            real_length += rsum_0
            omit_length += rsum_0

    real_length, omit_length = 32 - real_length, 32 - omit_length
    return real_length,omit_length
# 控制输入的IP前缀的个数
n = int(input())
ans = []
while n :
    pref = input()
    if pref.find('/') == -1:
        if pref.count('.') == 3:
            pref += '/'+ str(count_len(pref)[1]) #
        else:
            for i in range(3-pref.count('.')):
                pref += '.0'
            pref += '/' + str(count_len(pref)[1])
    elif pref.find('/') != -1:
        pre,rear = pref.split('/')
        if pre.count('.') == 3:
            pass
        else:
            for i in range(3-pre.count('.')):
                pre += '.0'
            pref = pre + '/' + rear
    ans.append(pref)
    n -= 1
temp = ''
ans.sort()
# 冒泡排序
for i in range(len(ans)):
    i_pre,i_rear = ans[i].split('/')
    for j in range(i+1,len(ans)):
        j_pre, j_rear = ans[j].split('/')
        if i_pre == j_pre:
            if int(i_rear) > int(j_rear):
                temp = ans[i]
                ans[i] = ans[j]
                ans[j] = temp
        else:
            break
# 输出
for i in range(len(ans)):
    print(ans[i])
for i in range(len(ans)):
    if ans[0] == '0.0.0.0/0':
        print(ans[0])
        break
    if i == 0:
        temp = ans[i].split('.')[0]
        print(ans[i])
    elif ans[i].split('.')[0] == temp:
        continue
    else:
        print(ans[i])
        temp = ans[i].split('.')[0]