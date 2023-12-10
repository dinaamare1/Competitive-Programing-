class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        result = []
        for path in paths:
            splited = path.split(" ")
            for i in range(1,len(splited)):
                for j in range(len(splited[i])):
                    if splited[i][j] == "(":
                        dic[splited[i][j+1:len(splited[i])+1]].append(splited[0]+ "/" + splited[i][:j])
        for files in dic.values():
            if len(files) > 1:
                result.append(files)
        return result

