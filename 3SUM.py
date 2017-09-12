def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n-2):
        if i==0 or nums[i]>nums[i-1]:
            sum_find = 0 - nums[i]
            low = i+1
            high = n-1

            while(low < high):
                if nums[low] + nums[high] == sum_find:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while (low < high and nums[low] == nums[low-1]): low+=1
                    while (low < high and nums[high] == nums[high + 1]): high-=1

                elif nums[low] + nums[high] < sum_find:
                    while low < high:
                        low += 1
                        if nums[low] > nums[low-1]: break
                else:
                    while low < high:
                        high -= 1
                        if nums[high] < nums[high+1]: break
    return res

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
