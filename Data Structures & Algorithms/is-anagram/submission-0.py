class Solution:
    def brute(self, s: str, t: str) -> bool:
        s_ascii, t_ascii = [], []
        for ch in s:
            s_ascii.append(ord(ch))
        for ch in t:
            t_ascii.append(ord(ch))
        s_ascii.sort()
        t_ascii.sort()
        return s_ascii == t_ascii
        
    def isAnagram(self, s: str, t: str) -> bool:
        return self.brute(s, t)