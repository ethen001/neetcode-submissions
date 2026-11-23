class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        delimeter = chr(256)
        for value in strs:
            encoded_str += f"{len(value)}{delimeter}{value}"
        return encoded_str;


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            digits = []
            while s[i].isdigit():
                digits.append(s[i])
                i += 1
            merged = "".join(digits)
            str_len = int(merged if merged.isnumeric() else 0)
            strs.append(s[i + 1:i + 1 + str_len])
            digits = []
            i = i + 1 + str_len
        return strs