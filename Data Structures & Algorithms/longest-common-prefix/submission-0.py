class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for i in range(len(strs[0])):
            for word in strs:

                if i >= len (word):
                    return prefix

                if word[i] != strs[0][i]:
                    return prefix

            prefix = prefix + strs[0][i]

        return prefix
            