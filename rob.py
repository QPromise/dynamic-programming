nums=[2,7,9,3,1]
def rob(nums,dp=0,n=len(nums)):
    """
    :type nums: List[int]
    :rtype: int
    """
    if n == 0:
        return nums[0]
    else:
        dp+=max(rob(nums,dp=dp+nums[n-2],n=n-2),rob(nums,dp=nums[n-1],n=n-1))
print(rob(nums))