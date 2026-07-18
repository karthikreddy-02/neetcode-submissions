class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_index_store = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in difference_index_store:
                return [difference_index_store[remainder], i]
            else:
                difference_index_store[nums[i]] = i
        

        