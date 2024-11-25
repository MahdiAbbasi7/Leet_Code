"""
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


def find(haystack: str, needle: str) -> int:
    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if haystack[i : i + n] == needle:
            return i
    return -1


print(find("leetcode", "leeto"))
