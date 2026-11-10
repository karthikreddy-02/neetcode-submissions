class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # we could sort both strings and compare if they are they same

        #another way is we can use Counter(s) == Counter(t)
        # if the counts are the same we will get the same result
        # we are comparing the dicts, I think that will the same results

        return Counter(s) == Counter(t)
        