"""
邏輯思路:
1. 先把IP依據"."分開
2. 再用join跟"[.]"合併
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        strr = "[.]"
        address = address.split(".")
        address = strr.join(address)
        return address

print(Solution().defangIPaddr("1.1.1.1"))