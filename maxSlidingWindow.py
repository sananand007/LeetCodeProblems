from collections import deque
def maxSlidingWindow(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        if nums==None or n==0 or n<k: return res

        q = deque()

        for i in range(n):
            while len(q) and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            if i < k-1:
                continue

            while len(q) and q[0]<=i-k:
                q.popleft()

            res.append(nums[q[0]])

        return res

def main():
    # Test cases
    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5

    print(maxSlidingWindow(nums,k))

if __name__=='__main__':
    main()
