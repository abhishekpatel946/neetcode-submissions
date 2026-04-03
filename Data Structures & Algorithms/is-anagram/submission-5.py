from collections import Counter

class Solution:
    def brute(self, s: str, t: str) -> bool:
        # TC = o(nlogn + mlogm), SC = o(n + m)
        s_ascii, t_ascii = [], []
        for ch in s:
            s_ascii.append(ord(ch))
        for ch in t:
            t_ascii.append(ord(ch))
        return s_ascii.sort() == t_ascii.sort()
    
    def better(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # rearrange
        i = k = 0
        t_arr = list(t)
        while k < len(s):
            j = i + 1
            if s[k] == t_arr[i]:
                i += 1
            else:
                while j < len(t_arr):
                    if s[k] == t_arr[j]:
                        # swap
                        t_arr[i], t_arr[j] = t_arr[j], t_arr[i]
                        i += 1
                        j += 1
                        break
                    j += 1
            k += 1
        # return
        return s == ''.join(t_arr)

    def optimal(self, s: str, t: str) -> bool:
        # # edge case
        # if len(s) != len(t):
        #     return False
        # # map
        # s_map = Counter(s)
        # t_map = Counter(t)
        # for k, v in s_map.items():
        #     if k not in t_map or t_map[k] != v:
        #         return False
        # return True

        # edge case
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True


    def isAnagram(self, s: str, t: str) -> bool:
        return self.optimal(s, t)