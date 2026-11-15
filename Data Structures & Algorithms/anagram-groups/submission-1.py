class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in sorted_anagrams:
                sorted_anagrams[sorted_word].append(word)
            else:
                sorted_anagrams[sorted_word] = [word]
        return list(sorted_anagrams.values())