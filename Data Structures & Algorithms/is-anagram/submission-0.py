class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # B1: Không quan tâm thứ tự — chỉ quan tâm mỗi ký tự xuất hiện bao nhiêu lần.
        # B2: Xác định Input/Output
        # B3: Nếu len(s) != len(t) thì sao? → chắc chắn False luôn! 
        #     Nếu đều là lowercase thì không cần check hoa/thường
        # B4: Nghĩ các hướng tiếp cận
        # - Hướng 1 — Sort rồi so sánh
        # - Hướng 2 — Đếm ký tự

        # Coding
        if len(s) != len(t):
            return False

        # Hướng 1:
        str_huong1 = sorted(s)
        str_huong2 = sorted(t)

        if str_huong1 == str_huong2:
            return True
        else: 
            return False

        # # Hướng 2:
        # str1 = {}
        # for char in s:
        #     if char in str1:
        #         str1[char] += 1
        #     else:
        #         str1[char] = 1

        # str2 = {}
        # for char in t: 
        #     if char in str2:
        #         str2[char] += 1
        #     else:
        #         str2[char] = 1 

        # # {'r': 2, 'a': 2, 'c': 2, 'e': 1} {'c': 2, 'a': 2, 'r': 2, 'e': 1}
        # if str1 == str2:
        #     return True
        # else:
        #     return False