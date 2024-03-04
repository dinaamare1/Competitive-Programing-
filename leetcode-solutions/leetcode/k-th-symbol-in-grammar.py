class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def change(n,k,val):
            nodes = 2 ** (n -1)
            if n == 1:
                return val
            if k > nodes//2:
                val = 1 if val == 0 else 0
                print(val)
                return change(n-1,k-nodes//2,val)

            else:
                val = 0 if val == 0 else 1
                return change(n-1,k,val)
        return change(n,k,0)

        