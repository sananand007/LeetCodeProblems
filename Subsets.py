def DFS(nums,ind,path,res):
    """
    rtype: void
    """
    res.append(path)
    for i in range(ind, len(nums)):
        DFS(nums,i+1,path+[nums[i]],res)
    return

def Subsets(A):
    """
    return all subsets of elements in list A
    """
    res = []
    path = []
    DFS(sorted(A),0,path,res)
    return res

A = [100,200,300]
print(Subsets(A))
