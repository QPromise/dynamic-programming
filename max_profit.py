prices=[7,1,5,3,6,4]
def maxProfit(prices):
    min_pri, max_pro = float("inf"), 0
    for i in range(len(prices)):
        min_pri = min(prices[i], min_pri)
        max_pro = max(prices[i] - min_pri, max_pro)
    return max_pro
print(maxProfit(prices))