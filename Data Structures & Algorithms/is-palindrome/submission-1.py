class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        # capture only strings
        for char in s:
            if char.isalpha() or char.isnumeric():
                ss += char.lower()
        # reverse and check
        return True if ss == ss[::-1] else False