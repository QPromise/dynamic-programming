#给出一组数，求这组数的间隔数的和的最大值
arr = [1, 2, 4, 1, 7, 8, 3]

def rec_opt(arr, i, hash={}):
    if i == 0:
        return arr[0]
    if i == 1:
        return max(arr[0], arr[1])

    if hash.get(i):
        value = hash[i]
    else:
        value = max(rec_opt(arr, i - 1), rec_opt(arr, i - 2) + arr[i])
        hash[i] = value
    return value

def dp_ort(arr):
    opt=[0]*len(arr)
    opt[0]=arr[0]
    opt[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        opt[i]=max(opt[i-1],opt[i-2]+arr[i])
    return opt[i]

print(rec_opt(arr, 6))
print(dp_ort(arr))