"""
邏輯流程:
1. 透過迴圈依序把nums拿出來
2. 把nums不斷/10 直到小於0為止
3. 計算除的次數 奇數次則該數的位數為奇數 反之則為偶數
"""
class Solution:
    def findNumbers(self, nums):
        old = 0
        even = 0
        for i in nums:
            
            #先取絕對值
            i = abs(i)
            times = 0
            while i >= 1:
                i /= 10
                times += 1
                
            #對2取於數==0則為偶數
            if times%2 == 0:
                even += 1
            else:
                old += 1
        return even

