#LeetCode
# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices) -> int:
        maxp = 0
        lmin = 100000
        lmax = 0
        for stock in prices:
            if lmin > stock:
                lmin = stock
                lmax = stock
            elif lmax < stock:
                lmax = stock
                maxp = max(maxp, lmax - lmin)
        return maxp

# checks
print(Solution.maxProfit(self = Solution, prices = [7,1,5,3,6,4]))
