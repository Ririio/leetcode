class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = []
        len1 = len(word1)
        len2 = len(word2)

        for i in range(max(len1, len2)):
            if i < len1:
                merge.append(word1[i])
            if i < len2:
                merge.append(word2[i])
        return ''.join(merge)