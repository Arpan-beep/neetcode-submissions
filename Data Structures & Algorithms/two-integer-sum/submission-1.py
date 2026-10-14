class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checklist = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in checklist:
                return [checklist[compliment],i]
            checklist[nums[i]] = i

        
        