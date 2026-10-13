class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        if len(s_counter) != len(t_counter):
            return False
        for item, count in s_counter.items():
            if not item in t_counter or t_counter[item] != count:
                return False
        return True