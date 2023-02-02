class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # create a dictionary where we are comparing the closing bracket to the opening bracket
        # instantiate a stack
        # loop through the characters of the string
        # if the character we looped through is in the dictionary (closing brackets(keys))
        # if the stack isn't empty and the last item in the stack is equal to the corresponding value of the dict[char]
        # we pop the stack
        # if the conditions aren't satisfied, then we know that the brackets are invalid
        # if the character we loop through isn't a key in the dictionary (opening brackets)
        # then we can append that character into the stack
        # return the boolean to see if the stack is empty or not

        dict = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in dict:
                if stack and stack[-1] == dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return stack == []

