# Leetcode Problem 720
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        word_set = set(words)
        d = collections.defaultdict(list)
        can_build = set()
        words.sort(key = len)
        print words
        for word in words:
            if len(word) == 1:
                can_build.add(word)
                d[1].append(word)
            else:
                if word[:-1] in can_build:
                    can_build.add(word)
                    d[len(word)].append(word)
        max_len = max(d.keys())
        return sorted(d[max_len])[0]
