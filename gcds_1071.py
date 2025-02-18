class Solution:
    def gcd(self, a: int, b: int) -> int:
        '''Calculate the greatest common divisor of a and b'''
        while b:
            # get the remainder of a/b, this makes b the larger of the two
            # thus we make a = b and b = a % b
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''Find the greatest common divisor of two strings'''
        # str1 + str2 should be equal to str2 + str1
        if str1 + str2 != str2 + str1:
            return ''
        
        # get the gcd of the lengths of the two strings
        gcd_length = self.gcd(len(str1), len(str2))
        return str1[:gcd_length]

