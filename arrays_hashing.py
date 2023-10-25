# 217. Contains Duplicate
# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def contains_duplicate(nums):
    # Time complexity =  O(n)
    # Space complexity = Linear
    hash = set()
    for i in nums:
        if i in hash:
            return True
        hash.add(i)
    return False

print(contains_duplicate([1,2,3, 1]))

# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def valid_anagram(s, t):
    #Time complexity = O(2n)
    #Space complexity = O(2n)
    if len(s) != len(t):
        return False
    
    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
    return count_s == count_t

print(valid_anagram("anagram", "nagaram"))

def valid_anagram2(s, t):
    #Time complexity = O(nlogn)
    #Space complexity = O(1) depending on sorting algorithm
    return sorted(s) == sorted(t)

print(valid_anagram2("anagram", "nagaram"))

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums, target):
    #Time complexity = O(n)
    #Space complexity = linear

    hash = {}

    for i in range(len(nums)):
        x = target - nums[i]
        if x in hash:
            return [hash[x], i]
        else:
            hash[nums[i]] = i

print(two_sum([2,7,11,15], 9))

# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

def k_freq(nums, k):
    #Time Complexity: O(n)
    #Space Complexity: O(n)

    hash = {}
    freq = [[] for i in range(len(nums) + 1)]
    final = []

    for i in nums:
        hash[i] = 1 + hash.get(i, 0)
    for x, y in hash.items():
        freq[y].append(x)
    
    for j in range(len(freq) - 1, 0, -1):
        for n in freq[j]:
            final.append(n)
            if len(final) == k:
                return final
print(k_freq([1,1,1,2,2,3], 2))