class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex == 0:
        #     return [1]
        # prev = self.getRow(rowIndex-1)
        # res = [1]
        # print(prev)
        # for i in range(1,len(prev)):
        #     res.append(prev[i-1]+prev[i])
        # res.append(1)
        # return res

        def Ptri(rowIdx):
            if rowIdx < 1:
                return [1]
            prev = Ptri(rowIdx-1)
            res = [1]
            for i in range(1,len(prev)):
                res.append(prev[i-1]+prev[i])
            res.append(1)
            return res
        return Ptri(rowIndex)

        