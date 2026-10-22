class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        arr = [[]for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] += 1
        
        for key,value in hashmap.items():
            arr[value].append(key)
        
        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)
            if k == len(res):
                return res





