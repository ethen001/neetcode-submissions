class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        delimeter = chr(256)
        for value in strs:
            encoded_str += f"{value}{delimeter}"
        return encoded_str;


    def decode(self, s: str) -> List[str]:
        strs = []
        original_str = []
        for c in s:
            if not c.isascii():
                strs.append("".join(original_str))
                original_str = []
            else:
                original_str.append(c)
        return strs