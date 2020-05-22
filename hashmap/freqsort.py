class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count up the occurances.
        counts = collections.Counter(s)

        # Build up the string builder.
        string_builder = []
        for letter, freq in counts.most_common():
            # letter * freq makes freq copies of letter.
            # e.g. "a" * 4 -> "aaaa"
            string_builder.append(letter * freq)
        return "".join(string_builder)