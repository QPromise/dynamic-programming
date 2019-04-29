import  numpy as np
arr=[3,34,4,12,5,2]
def rec_subset(arr,i,s):
    if s==0:
        return True
    if i==0:
        return arr[0]==s
    if arr[i]>s:
        return rec_subset(arr,i-1,s)
    return rec_subset(arr,i-1,s) or rec_subset(arr,i-1,s-arr[i])
print(rec_subset(arr,len(arr)-1,9))
print(rec_subset(arr,len(arr)-1,13))
def dp_subset(arr,S):
    subset=np.zeros((len(arr),S+1),dtype=bool)
    subset[:,0]=True#所有行的第0列，也就是第一行全为False
    subset[0,:]=False
    subset[0,arr[0]]=True
    for i in range(1,len(arr)):
        for s in range(1,S+1):
            if arr[i]>s:
                subset[i,s]=subset[i-1,s]
            else:
                subset[i,s]=subset[i-1,s] or subset[i-1,s-arr[i]]
    return subset[len(arr)-1,S]

arr=[0]
print(dp_subset(arr,9))