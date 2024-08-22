class Solution:
    def findComplement(self, num: int) -> int:
        print(num.bit_length())
        return num^(2**num.bit_length()-1)