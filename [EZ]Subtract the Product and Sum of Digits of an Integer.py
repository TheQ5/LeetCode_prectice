class Solution:
	def Product_of_digits(self, n):
		dig = []
		n = abs(n)
		while n >= 1:
			x = n%10
			n //= 10
			dig.append(x)
		for i in range(len(dig)-1):
			dig[0] = dig[0]*dig[i+1]
		return (dig[0])

	def Sum_of_digits(self, n):
		dig = []
		n = abs(n)
		while n >= 1:
			x = n%10
			n //= 10
			dig.append(x)
		for i in range(len(dig)-1):
			dig[0] = dig[0]+dig[i+1]
		return (dig[0])
	
	def subtractProductAndSum(self, n: int) -> int:
		ans = Solution().Product_of_digits(n) - Solution().Sum_of_digits(n)
		return(ans)

print(Solution().subtractProductAndSum(234))