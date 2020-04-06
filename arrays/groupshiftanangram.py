class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if len(strings) == 0:
		        return []

        str_map = dict()
        for s in strings:
            delta = ord(s[0]) - ord('a')
            k = "".join([chr(ord(c) - delta) if c >= s[0] else chr(26 + ord(c) - delta) for c in s])
            if k not in str_map:
                str_map[k] = list()
            str_map[k].append(s)

        print(str_map.keys())
        return str_map.values()