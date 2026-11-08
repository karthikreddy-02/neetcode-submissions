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
        Run time: O(N * log N), Space: O(N) -> for the sorted list

        option 2: we can use a set, keep adding values in there
        if we come across a value that is already in the set
        that means that there is a duplicate return True
        if it doesn't return true => return false

        Run time: O(N), Space: O(N) -> if no duplicates worst case you have 
        to store all values
 
        """

        visited = set()

        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        
        return False




        