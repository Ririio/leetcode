class Solution:
  def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    a_vowels = [char for char in s if char.lower() in vowels]
        
    a_vowels.reverse()
    count = 0
    return_val = ''
    
    for char in s:
      if char.lower() in vowels:
        return_val += a_vowels[count]
        count += 1
      else:
        return_val += char

    return return_val
    
if __name__ == '__main__':
  solution = Solution()
  print(solution.reverseVowels("IceCreAm"))