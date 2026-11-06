class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        length = len(nums)
        res = []

        for num in nums:
            hashmap[num] += 1

        bucket = [[] for i in range(length+1)]

        for key,value in hashmap.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

            






