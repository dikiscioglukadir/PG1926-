# -*- coding: utf-8 -*-
"""FizzBuzz Problemi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yMDTyGyKq7Tam4shj6ECWuFehMlsdSym
"""

class Solution(object):
    def FizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1,n+1):
            if i% 3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i %3==0:
                result.append("Fizz")
            elif i %5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

ob1 = Solution()
print(ob1.FizzBuzz(30))