# https://leetcode.com/problems/merge-sorted-array/submissions/1462087971/?envType=study-plan-v2&envId=top-interview-150


class Solution(object):
  def merge(self, nums1: list, m, nums2: list, n):
    nums1[m:] = nums2[:n]
    nums1.sort()



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)