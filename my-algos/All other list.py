
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets = set(nums)
        longest = 0

        for x in numsets:
            if x-1 not in numsets:
                length = 1
                while x+1 in numsets:
                    x = x+1
                    length += 1
                longest = max(longest, length)

        return longest
       

----------------------------------------------------------------------------------------------------
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0

        for x in nums:
            if x == 0:
                red += 1
            elif x == 1:
                white += 1
            elif x == 2:
                blue += 1

        for x in range(0, red, 1):
            nums[x] = 0
        for x in range(red, red+white, 1):
            nums[x] = 1
        for x in range(red+white, red+white+blue, 1):
            nums[x] = 2

 -------------------------------------------------------------------------------------------
 26. Remove Duplicates from Sorted Array
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        N = len(nums)
        left = 0        
        for i in range(0, N, 1):
            if nums[left] == nums[i]:
                continue
            elif nums[left] < nums[i]:
                left += 1
                nums[left] = nums[i]

        return left+1
----------------------------------------------------------------------------------------------
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for i, flower in enumerate(flowerbed):
      if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
        flowerbed[i] = 1
        n -= 1
      if n <= 0:
        return True

    return False    
-----------------------------------------------------------------------------------------------
