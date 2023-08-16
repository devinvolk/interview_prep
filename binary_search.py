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

# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and 
# eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and
# will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

from math import ceil
def koko(piles, h):
    l = 1
    r = max(piles)

    while l <= r:
        k = (r+l) // 2
        count = 0
        for bananas in piles:
            count += ceil(bananas/k)
        if count > h:
            l = k + 1
        else:
            r = k - 1
    return l

print(koko([3,6,7,11], 8))