class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # { giá_trị: index }

        for i, num in enumerate(nums):
            complement = target - num  # số cần tìm để cộng đủ target

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
# ⏱ Time: O(n) | Space: O(n)
'''

**Hình dung cách HashMap hoạt động:**
```
nums = [3, 4, 5, 6], target = 7

i=0, num=3 → cần tìm 7-3=4 → seen={} không có → lưu {3:0}
i=1, num=4 → cần tìm 7-4=3 → seen={3:0} CÓ!  → return [0, 1] ✅
'''