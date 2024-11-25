"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs: list[str]) -> str:
    ans = ""
    sortedStrs = sorted(strs)
    first, last = sortedStrs[0], sortedStrs[-1]
    print(first, last)
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


print(longestCommonPrefix(["dog", "racecar", "car"]))
