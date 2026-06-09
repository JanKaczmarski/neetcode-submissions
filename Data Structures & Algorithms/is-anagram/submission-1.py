class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0 for _ in range(ord('z') - ord('a') + 1)]
        
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1

        for val in cnt:
            if val != 0:
                return False 

        return True

        