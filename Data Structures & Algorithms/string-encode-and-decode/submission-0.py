class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for _str in strs:
            for char in _str:
                if char:
                    encrypted_char = ord(char)
                    enc += str(encrypted_char) + ','
            enc += str(ord('\n')) + ','
        return enc

    def decode(self, s: str) -> List[str]:
        curr_dec, res = "", []
        for char in s.split(','):
            if char:
                decrypted_char = chr(int(char))
                if decrypted_char == "\n":
                    res.append(curr_dec)
                    curr_dec = ""
                else:
                    curr_dec += decrypted_char
        return res
    