class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            frequency = [0]*26
            for char in s:
                index = ord(char) - ord('a')
                frequency[index] += 1
            result[tuple(frequency)].append(s)
        return list(result.values())