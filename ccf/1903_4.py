T,n = map(int,input().split(' '))
# print(T,n)
order = [] # 记录输入的指令值
for i in range(T*n):
    temp = input().split(' ')
    order.append(temp)
now_code_block = 0
end_code_block = 0
ans = [0] * T
for i in range(T*n):
    now_code_block = int(i / n)
    now_process = i % n # 当前属于第几个进程
    for j in range(len(order[i])):  # j = R1 etc.. order[i] = ['R1','R2'] etc..
        if order[i][j] == '':
            continue
        # print(now_process,order[i][j][1])
        # 直接没出现  死锁
        if order[i][j] != '': # 当前指令没使用过
            if 'R'+ order[i][j][1] in order[i]:
                for k in range (i+1,T*n):
                    end_code_block = int(k / n)
                    end_process = k % n
                    if now_code_block == end_code_block:
                        if end_process == int(order[i][j][1]):
                            if 'S' + str(now_process) in order[k]:
                                # 如果当前的是索引为0
                                if order[k].index('S' + str(now_process))== 0:
                                    order[i][j] = ''
                                    order[k][order[k].index('S' + str(now_process))] = ''
                                    break
                                for l in range(order[k].index('S' + str(now_process))):
                                    # 在当前索引前面还有没被置为空的值
                                    if order[k][l] != '':
                                        ans[end_process] = 1
                                        break
                                    # 都为空了，则该值有效
                                    else:
                                        order[i][j] = ''
                                        order[k][order[k].index('S' + str(now_process))] = ''
                                        break
                        else:
                            break
                    else:
                        break
        elif 'S'+ order[i][j][1] in order[i]:
            for k in range (i+1,T*n):
                end_code_block = int(k / n)
                end_process = k % n
                if now_code_block == end_code_block:
                    if end_process == int(order[i][j][1]):
                        if 'R' + str(now_process) in order[k]:
                            # 如果当前的是索引为0
                            if order[k].index('R' + str(now_process))== 0:
                                order[i][j] = ''
                                order[k][order[k].index('R' + str(now_process))] = ''
                                break
                            for l in range(order[k].index('R' + str(now_process))):
                                # 在当前索引前面还有没被置为空的值
                                if order[k][l] != '':
                                    break
                                # 都为空了，则该值有效
                                else:
                                    order[i][j] = ''
                                    order[k][order[k].index('R' + str(now_process))] = ''
                                    break
                    else:
                        break
                else:
                    break
for i in range(T):
    print(ans[i])