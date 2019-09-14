r,y,g = map(int,input().split(' '))
n = int(input())
time = 0
while n :
    # 记录走过路口还是红绿灯 需要的时间
    k,t = map(int,input().split(' '))
    if k == 0:
        time += t
    elif k == 1:
        time += t
    elif k == 2:
        time +=(t+r)
    elif k == 3:
        pass
    n -= 1
print(time)