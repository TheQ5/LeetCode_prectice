class Solution:
    def twoSum(self, target, nums=[]): ##有預設值的要放後面
        times = 0
        for i in nums:
            for j in nums[times+1:]:
                if i + j == target:
                    a = nums.index(i) ##index可以找出
                    b = nums.index(j)
                    return[a, b]
                times += 1

x = Solution()
ans = x.twoSum(9, [2, 7, 11, 15])
print(ans)