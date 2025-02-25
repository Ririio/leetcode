from typing import List

class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		count = 0
		# Iterate through the flowerbed
		for i in range(len(flowerbed)):
			# Only check if the current iteration is 0
			if flowerbed[i] == 0:
				# Ensure that there is no out of bounce for each placement
				left_placement = (i == 0) or (flowerbed[i - 1] == 0)
				right_placement = ((len(flowerbed) - 1) == i) or (flowerbed[i + 1] == 0)

				if left_placement and right_placement:
					flowerbed[i] = 1
					count += 1
		return count >= n

if __name__ == '__main__':
	solution = Solution()
	print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))