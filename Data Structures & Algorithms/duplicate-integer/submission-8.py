class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """"
        given: integer array
        return: any value that appears more than once -> true, else false

        integer values? : -10**9 to 10**9
        length: 0 <= len(nums) <=10**5

        option 1: we can sort and compare the current value with previous
        if they match: break, return true
        if it doesn't return true, no duplicates -> return false
 
        """

        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False
        

        