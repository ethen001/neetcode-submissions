class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        answer = []
        limit = k
        for key, value in sorted_count:
            if limit == 0:
                break
            answer.append(key)
            limit -= 1
        return answer