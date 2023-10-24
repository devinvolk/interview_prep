# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def buy_sell(prices):
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    left = 0
    right = 1
    profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            test = prices[right] - prices[left]
            if test > profit:
                profit = test
        else:
            left = right
        right += 1
    return profit

print(buy_sell([7,1,5,3,6,4]))

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def longest_no_repeat_substring(s):
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    
    test = set()
    length = 0
    l = 0

    for r in range(len(s)):
        while s[r] in test:
            test.remove(s[l])
            l += 1
        test.add(s[r])
        length = max(length, r - l + 1)
    return length

print(longest_no_repeat_substring("pwwkew"))