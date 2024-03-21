class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        n = len(s)
        char_dict = {}
        left, right = 0, 0
        max_len = 0
        
        while right < n:
            if s[right] in char_dict and char_dict[s[right]] >= left:
                left = char_dict[s[right]] + 1
            char_dict[s[right]] = right
            right += 1
            max_len = max(max_len, right - left)

        return max_len