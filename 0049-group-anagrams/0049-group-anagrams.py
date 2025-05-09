class Solution(object):
    def groupAnagrams(self, strs):
        anagramDict = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr not in anagramDict:
                anagramDict[sortedStr] = []
            anagramDict[sortedStr].append(str)
        return list(anagramDict.values())
