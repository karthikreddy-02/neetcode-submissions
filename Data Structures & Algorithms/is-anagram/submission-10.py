class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # we could sort both strings and compare if they are they same

        return sorted(s) == sorted(t)
        
        