class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        words = set(wordDict)


        for j in range(len(s) - 1, -1, -1):
            for i in range(j, -1, -1):
                if s[i:j + 1] in words:
                    dp[i] = dp[i] or dp[j + 1]
        return dp[0]


