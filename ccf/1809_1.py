n = int(input()) # 商店的数量
prices = list(map(int,input().split(' ')))
# prices = [int(i) for i in input().split(' ')] # 每个商店第一天的价格
new_prices = [0] * n # 每个商店第二天的新价格
for i in range(len(prices)):
    if i == 0: # 如果是第一个店铺
        new_prices[i] = (prices[i] + prices[i + 1]) // 2
    elif i == len(prices) - 1: # 如果是最后一个
        new_prices[i] = (prices[i] + prices[i - 1]) // 2
    else: # 中间店铺
        new_prices[i] = (prices[i - 1] + prices[i] + prices[i + 1]) // 3
for i in range(len(new_prices)): # 输出新价格 空格连续
    if i != len(new_prices) - 1:
        print(new_prices[i],end=' ')
    else:
        print(new_prices[i],end='')