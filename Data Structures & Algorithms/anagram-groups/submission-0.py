class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hm = {}

        for i in range(len(strs)):
            string = strs[i]
            key = ''.join(sorted(string))

            if key not in hm:
                hm[key]= len(res)
                res.append([])
            
            res[hm[key]].append(strs[i])

        return res