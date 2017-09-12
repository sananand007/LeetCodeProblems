def MajorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums==None: return None
    nums.sort()

    count=0
    n = len(nums)
    candidate = nums[n//2]

    for num in nums:
        if num==candidate:
            count+=1

    if count>=(n+1)//2:
        return candidate

    return -1

nums = [1,1,1,100]
print(MajorityElement(nums))
