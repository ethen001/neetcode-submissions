class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
          buckets[count].append(num)
        answer = []
        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                if len(answer) < k:
                    answer.append(num)
        return answer