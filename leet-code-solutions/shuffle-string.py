class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""]*len(indices)
        for indice in range(len(indices)):
            result[indices[indice]] = s[indice]
            print(result )
        return "".join(result)