class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
          winL, maxLen, common = 0, 0, 0
          charMap = dict()

          for winR in range(len(s)):
            rightChar = s[winR]
            if rightChar not in charMap:
              charMap[rightChar] = 0
            charMap[rightChar] += 1

            common = max(common, charMap[rightChar])

            if (winR - winL + 1 - common) > k:
              charMap[s[winL]] -= 1
              winL += 1

            maxLen = max(maxLen, winR - winL + 1)

          return maxLen