class Solution(object):
    """docstring for Solution."""
    def __init__(self):
        super(Solution, self).__init__()
    def returnindex2(self, nums, k, si):
            n,cycle = len(nums),[]
            if si<0 or si>(n-1):
                return -1
            else:
                nextstep = si
                cycle.append(si)
                while k!=0:
                    nextstep = nums[nextstep]
                    if nextstep in cycle:
                        #cycle detected
                        break
                    cycle.append(nextstep)
                    k-=1
                #print("debug",nextstep,k,cycle)
                if k==0:
                    return nextstep
                else:
                    return cycle[-1] if k%2==0 else cycle[-2]


obj=Solution()
print(obj.returnindex2([1,3,0,1,4,2], 500000, 2))
