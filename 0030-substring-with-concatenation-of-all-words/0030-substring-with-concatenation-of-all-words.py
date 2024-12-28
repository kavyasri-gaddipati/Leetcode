from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        # We can try starting from each index i from 0 to len(s) - total_len
        for i in range(word_len):  # We will try starting from i = 0, 1, ..., word_len-1
            left = i
            right = i
            window_freq = Counter()
            count = 0

            # Slide the window
            while right + word_len <= len(s):
                # Extract the word at the 'right' position
                word = s[right:right + word_len]
                right += word_len

                # If the word is in words, update the window
                if word in word_freq:
                    window_freq[word] += 1
                    count += 1

                    # If the word frequency exceeds the target frequency, move the left pointer
                    while window_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        window_freq[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If we have found a valid window
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset the window if the word is not in the list of words
                    window_freq.clear()
                    count = 0
                    left = right

        return result
