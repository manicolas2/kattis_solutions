class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        reps = []
        cout = 0
        for i in s:
            if i in reps:
                return cout
            else:
                reps.append(i)
                cout += 1

if __name__ == "__main__":
    sol = Solution()
    res = sol.lengthOfLongestSubstring("pwwkew")
    print(res)