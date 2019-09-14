n = int(input())
h_time = set()
w_time = set()
count = 0
for i in range(n):
    begin, end = input().split(' ')
    begin = int(begin)
    end = int(end)
    for j in range(begin, end):
        h_time.add(j)
for i in range(n):
    begin, end = input().split(' ')
    begin = int(begin)
    end = int(end)
    for j in range(begin, end):
        w_time.add(j)
print(h_time,w_time)


n = int(input())
q = n
h = []
m = []
while n:
    h.append([int(i) for i in input().split(' ')])
    n -= 1
while q:
    m.append([int(i) for i in input().split(' ')])
    q -= 1
t = 0
k = 0
temp = 0
for i in range(len(h)):
    for j in range(k,len(m)):
        temp = min(h[i][1], m[j][1]) - max(h[i][0], m[j][0])
        if (temp <= 0):
            continue
        else:
            t += temp # if (min(h[i][1],m[j][1]) - max(h[i][0],m[j][0])) >= 0 else 0
            k = j
print(t)

