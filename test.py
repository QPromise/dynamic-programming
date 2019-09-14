#正常递归
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)
#哈希存储
def hash_fib(i,hash={}):
    if i < 2:
        return 1
    if hash.get(i):
        return hash[i]
    else:
        value = fib(i-1) + fib(i-2)
        hash[i] = value
        return value

print(hash_fib(4))
print(fib(4))