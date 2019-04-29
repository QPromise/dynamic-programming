def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i - 1], nums[i])
        return max(dp)

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))