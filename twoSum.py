"""
邏輯流程:
1. 透過迴圈把list輪一遍
2. 如果target - nums不在字典裡 則存進字典
3. 如果在字典裡 就提取出來

存字典的目的:
1. 可以避免list中單筆資料被提取兩次
    EX: [3, 2, 4] target=6 則3就會被提兩次而回傳[0, 0]但正解是[1, 2]
2. 可以解決list中如果有兩筆相同數值的資料
    EX: [3, 3] target=6 

缺點:
多一個字典的儲存空間
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target-nums[i]], i]