class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        split_str = s.split()
        for word in range(len(split_str)):
            if word < len(split_str) - 1:
                output += split_str[word][::-1] + " "
            else: 
                output += split_str[word][::-1]
        return output