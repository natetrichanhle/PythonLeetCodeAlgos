class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create two dictionaries with the key value pairs. One for s and one for t
        # compare those two dictionaries to see if they're equal

        # 1st attempt
        s_dict = {}
        t_dict = {}
        # base case - if the lengths of the two strings are not equal then we know that it's not an anagram
        if len(s) != len(t):
            return False
        # add the key value pairs of s into a dictionary
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        # add the key value pairs of t into a dictionary
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        # return the compared boolean of the two dictionaries
        return s_dict == t_dict
        
        