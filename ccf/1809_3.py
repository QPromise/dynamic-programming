"""
11 1
html
..head
....title
..body
....h1
....p #subtitle
....div #main
......h2
......p #one
......div
........p #two
"""
n,m = map(int,input().split(' '))
#print(n,m)
contents = []
while n : # 结构化文档的内容 .... div #123456
    temp = input()
    prior = temp.count('.') // 2 # 优先级
    temp = temp[temp.rfind('.')+1:] # 截取结构内容
    if temp.find('#') != -1: # 如果有id
        flag,id = temp.split(' ')
    else: # 如果没有id
        flag,id = temp,None
    content = {'prior':prior,'flag':flag.lower(),'id':id} # 这一行结构化内容的表示
    #print(line)
    contents.append(content)
    n -= 1
#print(contents)
ans = []
while m :
    sum = 0
    line = 0
    now = []
    temp = input() # 输入选择
    if temp.find('#') != -1: # id选择
        if temp.find('#') == 0: # 只有id
            for i in range(len(contents)):
                if contents[i]['id'] == temp:
                    sum += 1
                    line = i+1
                    break
            now.append(sum)
            now.append(line)
        elif temp.count(' ') == 1: # 一个标签 一个id
            flag,id = temp.split(' ')
            for i in range(len(contents)):
                if contents[i]['id'] == id and contents[i]['flag'] == flag.lower():
                    sum += 1
                    line = i+1
                    break
            now.append(sum)
            now.append(line)
        else: # 一个标签 一个id  多个后代 第二个循环只需要执行一遍
            flags = [flag for flag in temp.split(' ') ]
            for i in range(len(flags)):
                if flags[i].find('#') == -1:
                     flags[i] = flags[i].lower()
            count = 0
            k = 0
            for i in range(len(flags)):
                if i == 1: # 跳过id
                    continue
                # print(i,flags[i])
                for j in range(k,len(contents)):
                    # print(i,k)
                    if i == 0:
                        if flags[0] == contents[j]['flag'] and flags[1] == contents[j]['id']:
                            k = j+1
                            break
                    elif flags[i] == contents[j]['flag'] and (i+1) == contents[j]['prior'] or flags[i] == contents[j]['flag'] and (i+1) <= contents[j]['prior']:
                        k = j + 1
                        if i == len(flags) - 1:
                            sum += 1
                            line = j + 1
                            now.append(line)
                        break
            now.insert(0,sum)
        #print(now)
    elif temp.find(' ') != -1: # 后代选择
        flags =[flag.lower() for flag in temp.split(' ')]
        # print(flags)
        count = 0
        k = 0 # 记录下一次的起始位置
        while True:
            for i in range(len(flags)):
                # print(i,flag)
                for j in range(k,len(contents)):
                    # print(i,k)
                    if flags[i] == contents[j]['flag'] and (i+2) == contents[j]['prior'] or flags[i] == contents[j]['flag'] and (i+2) <= contents[j]['prior']:
                        count += 1
                        k = j + 1
                        break
             # 如果计数满一遍了
            if count == len(flags):
                sum += 1
                line = j + 1
                count = 0
                now.append(line)
            if count != len(flags) and j == len(contents) - 1:
                now.insert(0, sum)
                break
    else: # 标签选择 不区分大小写
        for i in range(len(contents)):
            if contents[i]['flag'] == temp.lower():
                sum += 1
                line = i+1
                now.append(line)
        now.insert(0,sum)
        #print(now)
    ans.append(now)
    m -= 1
# print(ans)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end=' ')
    print()