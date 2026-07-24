class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. convert string to ascii value in int format
        s_num, t_num = [], []
        for i in s:
            s_num.append(int(ord(i)))
        for j in t:
            t_num.append(int(ord(j)))
        
        # 2. sort the arrays & return
        print(s_num, t_num)
        s_num = sorted(s_num)
        t_num = sorted(t_num)
        return s_num == t_num
