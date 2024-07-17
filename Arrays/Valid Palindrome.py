'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        n_s = []
        s = s.lower().split(' ')
        s = ''.join(s)

        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz' or letter in '0123456789':
                n_s.append(letter)
        
        campare_s = ''.join(n_s)

        n_s = n_s[::-1]
        n_s = ''.join(n_s)


        if campare_s ==  n_s :
            return True
        else:
            return False


obj = Solution()
print(obj.isPalindrome('race a car'))