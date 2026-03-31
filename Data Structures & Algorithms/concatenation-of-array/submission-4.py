class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num_length = len(nums)
        ans = [0] * (2 * num_length)
        if 1 <= num_length <= 1000:
            for i in range(len(nums)):
                ans[i] = nums[i]
                ans[i + num_length] = nums[i]

        return ans