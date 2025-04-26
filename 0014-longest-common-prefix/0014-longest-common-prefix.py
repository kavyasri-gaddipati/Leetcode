class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        first=strs[0]
        last=strs[-1]
        result=[]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                break 
            result.append(first[i]) 
        return ''.join(result)    

        