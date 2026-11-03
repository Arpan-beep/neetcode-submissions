class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        
        for s in strs:
            sortedword = ''.join(sorted(s))
            if sortedword not in hashmap:
                hashmap[sortedword] = len(res)
                res.append([])
            
            res[hashmap[sortedword]].append(s)
        
        return res
