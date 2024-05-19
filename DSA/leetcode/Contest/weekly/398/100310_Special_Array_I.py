"""

100310. Special Array I
User Accepted:17207
User Tried:17632
Total Accepted:17969
Total Submissions:23913
Difficulty:Easy




An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

Example 1:

    Input: nums = [1]
    Output: true

    Explanation:
    There is only one element. So the answer is true.

Example 2:

    Input: nums = [2,1,4]
    Output: true

    Explanation:
    There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

    Input: nums = [4,3,1,6]
    Output: false

    Explanation:
    nums[1] and nums[2] are both odd. So the answer is false.

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

"""


class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums)==1:
            return True
        
        if nums[0]%2==1:
            check_odd = True
            for i in range(0, len(nums), 2):
                if nums[i]%2==0:
                    check_odd=False
                    break
            check_even = True
            for i in range(1, len(nums), 2):
                if nums[i]%2==1:
                    check_even=False
                    break
        else:
            check_even = True
            for i in range(0, len(nums), 2):
                if nums[i]%2==1:
                    check_even=False
                    break
            check_odd = True
            for i in range(1, len(nums), 2):
                if nums[i]%2==0:
                    check_odd=False
                    break
                    
        return check_odd and check_even
    


solution = Solution()
# [1]
# list = [2, 1, 4]
list = [4,3,1,6]
isSpecial = solution.isArraySpecial(list)
print(f'is Array special: {isSpecial}')




