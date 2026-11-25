class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)
        # calculate the prefix products
        for i in range(n): 
            prefix[i + 1] = prefix[i] * nums[i]
        # calculate the suffix products
        for i in range(n-1,-1, -1):
            suffix[i] = suffix[ i + 1] * nums[i]
        # calculate the answer
        results = []
        for i in range(n):
            results.append(prefix[i] * suffix[i + 1])
        return results