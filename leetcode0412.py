#LeetCode
#412. Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
#   answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#   answer[i] == "Fizz" if i is divisible by 3.
#   answer[i] == "Buzz" if i is divisible by 5.
#   answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int):
        answear = [None] * n
        for i in range(n):
            if (i+1) % 3 == 0:
                answear[i] = "Fizz"
                if (i+1) % 5 == 0:
                    answear[i] = "FizzBuzz"
            elif (i+1) % 5 == 0:
                    answear[i] = "Buzz"
            else:
                answear[i] = str(i+1)
        return answear
      
print(Solution.fizzBuzz(self = Solution, n = 15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])