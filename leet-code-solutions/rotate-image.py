class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        n = len(matrix)
        tp = [0,0]
        bp = [n-1,0]
        while tp[0]<bp[0]:
            while tp[1]< n:
                matrix[tp[0]][tp[1]],matrix[bp[0]][bp[1]] = matrix[bp[0]][bp[1]],matrix[tp[0]][tp[1]]
                tp[1] += 1
                bp[1] += 1
            tp[0] += 1
            bp[0] -= 1
            tp[1] = 0
            bp[1] = 0
        for i in range(n-1):
            pt = [i, i]
            for j in range(n-i):
                matrix[pt[0]+j][pt[1]], matrix[pt[0]][pt[1]+j] = matrix[pt[0]][pt[1]+j], matrix[pt[0]+j][pt[1]]


        # n = len(matrix)
        # swap = n
        # for i in range(n//2):
        #     tl = [i,i]
        #     bl = [n-1-i,i]
        #     tr = [i,n-1-i]
        #     br = [n-1-i,n-1-i]
        #     for _ in range(swap-1):
        #         matrix[tl[0]][tl[1]],matrix[bl[0]][bl[1]] = matrix[bl[0]][bl[1]],matrix[tl[0]][tl[1]]
        #         matrix[tr[0]][tr[1]],matrix[br[0]][br[1]] = matrix[br[0]][br[1]],matrix[tr[0]][tr[1]] 
        #         matrix[bl[0]][bl[1]],matrix[tr[0]][tr[1]] = matrix[tr[0]][tr[1]],matrix[bl[0]][bl[1]]
        #         tl[0] +=1
        #         bl[1] += 1
        #         tr[1] -= 1
        #         br[0] -= 1
        #     swap -= 2
        