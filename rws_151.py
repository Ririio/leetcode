class Solution:
  def reverseWords(self, s: str) -> str:
    words = s.split()
    words.reverse()
    return_value = ''
    for i, word in enumerate(words):
      if i != len(words) - 1:
        return_value += f"{word} "
        continue
      return_value += word

    return return_value
  
if __name__ == '__main__':
  solution = Solution()
  print(solution.reverseWords('the sky is blue'))
  print(solution.reverseWords("a good   example"))