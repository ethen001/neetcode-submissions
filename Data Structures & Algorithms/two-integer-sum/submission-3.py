class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, value in enumerate(nums):
            j_val = target - value
            if j_val in nums_dict:
                return [nums_dict[j_val], i]
            else:
                nums_dict[value] = i