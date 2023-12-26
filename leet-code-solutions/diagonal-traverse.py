class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        ans = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                dic[row+col].append(mat[row][col])
        for key in dic:
            if key % 2:
                for val in dic[key]:
                    ans.append(val)
            else:
                for val in dic[key][::-1]:
                    ans.append(val)
        return ans
        # ans = []
        # cur_row,cur_col = 0,0
        # row = len(mat)
        # col = len(mat[0])
        # length = row * col
        # upFlag = True             
        # # while len(ans)<length:
        # #     if upFlag:
        # #         while cur_row>=0 and cur_col<col:
        # #             ans.append(mat[cur_row][cur_col])
        # #             cur_row -= 1
        # #             cur_col += 1
        # #         if cur_col == col:
        # #             cur_row += 2
        # #             cur_col -= 1
        # #         else:
        # #             cur_row += 1
        # #         upFlag = False
        # #     else:
        # #         while cur_row<row and cur_col>=0:
        # #             ans.append(mat[cur_row][cur_col])
        # #             cur_row += 1
        # #             cur_col -= 1
        # #         if cur_row == row:
        # #             cur_row -= 1
        # #             cur_col += 2
        # #         else:
        # #             cur_col += 1
        # #         upFlag = True
        # # return ans


        