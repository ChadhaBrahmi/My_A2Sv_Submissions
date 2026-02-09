class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        a = ""
        first = strs[0]

        for i in range(len(first)):
            char = first[i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return a
            a += char

        return a
