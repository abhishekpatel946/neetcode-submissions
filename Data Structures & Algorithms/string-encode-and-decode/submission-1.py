class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, idx = [], 0
        while idx < len(s):
            j = idx
            while s[j] != "#": j += 1 
            length = int(s[idx : j])
            res.append(s[j + 1: j + 1 + length])
            idx = j + 1 + length
        return res
    