class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            j_value = target - nums[i]
            if j_value in nums_dict:
                j = nums_dict[j_value]
                return [j, i]
            else:
                nums_dict[nums[i]] = i