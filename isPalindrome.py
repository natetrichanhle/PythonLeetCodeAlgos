class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove the non-alphanumeric characters
        # convert the string to lower case
        # compare if the new string is the same as the string reversed
        
        # 1st solution --> more efficient

        # create a new string to push the alphanumerical characters in
        new_str = "" 
        # loop through the characters in s
        for char in s:
        # if it is alphanumeric you want to add that to the new string, but don't forget to lowercase it
            if char.isalnum():
                new_str += char.lower()
        # return the boolean if the new_str is equal to itself, but reversed. Then we know if it's a palindrome or not
        return new_str == new_str[::-1]

        # 2nd solution --> using ascii table

        # create a helper function to see if a character is alpha numeric
        # instantiate your two pointers left and right (left:start, right:end)
        # loop through the string until either left has crossed the right pointer or they meet in the middle
        # loop to check if the characters you're on are alphanumeric, if so then shift pointers
        # check if the characters are the same, & if not return false
        # if the loop is executed thoroughly, then you know that the string is a palindrome
        
        # def alphaNumeric(char):
        #     return (ord('A') <= ord(char) <= ord('Z') or
        #             ord('a') <= ord(char) <= ord('z') or
        #             ord('0') <= ord(char) <= ord('9'))

        # left, right = 0, len(s) - 1
        # while left <= right:
        #     while left < right and not alphaNumeric(s[left]):
        #         left += 1
        #     while right > left and not alphaNumeric(s[right]):
        #         right -=1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left, right = left + 1, right - 1
        # return True

