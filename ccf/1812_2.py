r,y,g = map(int,input().split(' '))
n = int(input())
time = 0
while n :
    # 记录走过路口还是红绿灯 需要的时间
    k,t = map(int,input().split(' '))
    if k == 0:
        print(t)
        time += t
    elif k == 1:
        if time < (t + y):
            print((t + y - time))
            time += (t + y - time)
        else:
            if (time - (t + y )) % (g + y + r) in range(g,g + y + r + 1):
                print(((y + r) - (time - (t + y )) % (y + g + r) + g))
                time += ((y + r) - (time - (t + y )) % (y + g + r) + g)
            else:
                pass
    elif k == 2:
        if time < (t + r) :
            print((t+r)  - time)
            time += ((t + r)  - time)
        else:
            if (time - (t + r)) % (g + r + y) in range(g,g + y + r + 1):
                print(((y + r) - (time - (t + r)) % (y + g + r) + g))
                time += ((y + r) - (time - (t + r)) % (y + g + r) + g)
            else:
                pass
    elif k == 3:
        if time < t :
            pass
        if (time - t) % (y + r + g) in range(0, y + r + 1):
            print(((y + r) - (time - (t)) % (y + g + r)))
            time += ((y + r) - (time - (t)) % (y + g + r))
        else:
            pass
    n -= 1
print(time)