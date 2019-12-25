class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		a = 0
		b = 1
		for i in str(n):
			i = int(i)
			a = a + i
			b = b * i
		return(b-a)

print(Solution().subtractProductAndSum(234))