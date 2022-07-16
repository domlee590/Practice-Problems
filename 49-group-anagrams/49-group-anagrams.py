class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anaMap = defaultdict(list)
        
        for word in strs:
            charCount = [0 for i in range(26)]
            for char in list(word):
                charCount[ord(char) - ord("a")] += 1
            anaMap[tuple(charCount)].append(word)
        
        return anaMap.values()