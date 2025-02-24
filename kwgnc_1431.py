from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      max_candy = max(candies)
      results = []
      for candy in candies:
        results.append((candy + extraCandies) >= max_candy)
      
      return results

if __name__ == '__main__':
  solution = Solution()
  print(solution.kidsWithCandies([2,3,5,1,3], 3))
  