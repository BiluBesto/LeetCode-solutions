class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cstr = strs[0]
        strs = strs[1:]
        for i in strs:
            ct = 0
            for j in i:
                if ct < len(cstr) and j == cstr[ct]:
                    ct = ct + 1
                    continue
                else:
                    break
            cstr = cstr[0:ct]
        return cstr

