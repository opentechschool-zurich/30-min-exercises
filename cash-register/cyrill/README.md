# Compute Change

The objective of this exercise is to compute the minimum pieces of currency to
represent a given sum of money.

This problem can be solved under the assumption of unlimited or limited
currency.

## Solution

This problem is similar to the unbounded knapsack problem (UKP) if the amount
of available currency is infinte or the bounded knapsack problem (BKP) if there
is a limited amount of currency. The greedy algorithm gives good approximate
solutions for both problems. In some scenarios however it won't find a solution
even if there is one.

For example: given denominations of 3 and 2 and an amount of 4 the greedy
algorithm will fail to find a solution. When it subtracts 3 from 4 it gets 1
which is unrepresentable using the given denominations.

One solution is to backtrack and try with the next smaller denomination if no
solution can be find to a sub problem.

## Files

- greedy_ukp.py -- Implements the naïve approach to the UKP variant of the problem.
- greedy_bkp.py -- Implements the naïve approach to the BKP variant of the problem.
- greedy_with_backtracking_bkp.py -- Uses backtracking to find more solutions to the BKP variant of the problem.
- register.py -- Text based user interface for comparing the three approaches.
