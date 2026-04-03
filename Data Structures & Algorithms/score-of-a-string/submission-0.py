class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        # iterate over the string of chars
        for i in range(0, len(s) - 1):
            # get the ascii value and store sum of abs
            res += abs(ord(s[i+1]) - ord(s[i]))
        # return
        return res