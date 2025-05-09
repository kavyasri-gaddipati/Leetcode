class Solution(object):
    def removeAnagrams(self, words):
        def areAnagrams(str1,str2):
            return sorted(str1)==sorted(str2)

        i=1 
        while i<len(words):
            if areAnagrams(words[i-1],words[i]):
                words.pop(i)
            else:
                i+=1
        return words
        