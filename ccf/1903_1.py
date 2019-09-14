import math
n = int(input())
num = list(map(int,input().split(' ')))
max_,min_ = max(num),min(num)
mid_ = 0
if n % 2 == 0:
    mid = (num[n//2] + num[n//2 - 1]) / 2
    mid_ = (num[n//2] + num[n//2 - 1]) // 2
    if mid != mid_:
        mid = round(mid,1)
    else:
        mid = int(mid)
else:
    mid = num[n//2]
count = 0
ans = [max_,min_,mid]
ans = sorted(ans,reverse = True)
for i in ans:
    print(i,end=" ")