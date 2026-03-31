class Solution:
    '''
    nums = [1, 2, 3, 3]
    set(nums)  →  {1, 2, 3}    # 3 bị loại 1 cái
    len(nums) = 4 != len(set(nums)) = 3  →  True ✅
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))