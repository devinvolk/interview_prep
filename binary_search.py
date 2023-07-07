# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, 
# then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r)//2

        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

print(binary_search([-1,0,3,5,9,12], 9))

# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def search_2d(matrix, target):
    for i in matrix:
        if i[-1] >= target:
            l = 0
            r = len(i) - 1
            while l <= r:
                m = (l + r)//2
                if i[m] == target:
                    return True
                elif i[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False

print(search_2d([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 16))