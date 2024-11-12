class Solution:
    def frequencySort(self, s: str) -> str:
        out = ''
        data = Counter(s).most_common()
        for key, value in data:
            out += key*value
        return out