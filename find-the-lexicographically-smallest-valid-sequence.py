class Solution:
    def validSequence(self, word1: str, word2: str):
        n, m = len(word1), len(word2)
        if m > n:
            return []
        suf = [0] * (n + 1)
        j = m
        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            suf[i] = m - j

        result = []
        i = j2 = 0
        mistake_used = False

        while j2 < m:
            if i >= n:
                return []
            if word1[i] == word2[j2]:
                result.append(i)
                i += 1
                j2 += 1
            elif not mistake_used and suf[i + 1] >= m - j2 - 1:
                result.append(i)
                mistake_used = True
                i += 1
                j2 += 1
            else:
                i += 1

        return result