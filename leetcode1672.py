#LeetCode
#1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts) -> int:
        k = 0
        for i in range(len(accounts)):
            k = max(k, sum(accounts[i]))
        return k

#checking
print(Solution.maximumWealth(self = Solution, accounts= [[2,8,7],[7,1,3],[1,9,5]]) == 17)