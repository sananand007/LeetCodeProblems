def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def DFS(res, path, myDict, start, depth):
            if depth==len(digits):
                res.append(path)
                return
            for i in range(start, len(myDict[digits[depth]])):
                DFS(res, path + myDict[digits[depth]][i], myDict, 0, depth+1)

            return

        myDict = {'0':[' '], '1':['*'], '2': list('abc'), '3': list('def'), '4': ('ghi'),
        '5': list('jkl'), '6': list('mno'), '7': list('pqrs'), '8': list('tuv'), '9': list('wxyz')}

        res = []
        path = ''

        DFS(res, path, myDict, 0, 0)
        return res

digits = "2312"
print( letterCombinations(digits))
