# Programming-Assignment-3

## Student Info
- **Name:** Tess Jaworski
- **UFID:** 33286422

## Build Instructions
No compilation required. Requires Python 3.

## How to Run
python3 src/hvlcs.py data/example.in

## Assumptions
- Character values are non-negative integers

## Written Component
**1.Empirical Comparison**

<img width="3000" height="1800" alt="runtime_graph" src="https://github.com/user-attachments/assets/a00ecdb0-12a0-4d17-b746-3df6d91ab179" />

**2.Recurrence Equation**

dp[i][j] is the max value of a common subsequence using first i characters of A and first j characters of B

Base cases:
dp[0][j] = 0 (empty string A)
dp[i][0] = 0 (empty string B)

Recurrence:

If A[i] = B[j]:

	dp[i][j] = max(dp[i-1][j-1] + value(A[i]), dp[i-1][j], dp[i][j-1])

  
Else:

	dp[i][j] = max(dp[i-1][j], dp[i][j-1])

This recurrence is correct because it handles all the possible cases.The optimal solution must either include the match at i and j or skip at least one character. We consider all possibilities and take the maximum which is guaranteed to be the optimal value. 

Case 1: characters match (A[i] = B[j])

  - Case 1a: take the match and add its value to the solution
  - Case 1b: skip A[i]
  - Case 1c: skip B[j]

Case 2: characters don't match (A[i] != B[j])

  - Case 2a: Skip A[i]
  - Case 2b: Skip B[j]


**3.Big-Oh**

pseudocode:

HVLCS(A, B, values):

    m = len(A)
    n = len(B)
    Initialize table dp[0...m][0...n]
    
    for i = 1 to m:
        for j = 1 to n:
            if A[i] == B[j]:
                dp[i][j] = max(dp[i-1][j-1] + values[A[i]],
                              dp[i-1][j],
                              dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

Runtime is O(mn) because the outer loop runs m times and the inner loop runs n times. There are mn iterations and each iteration is O(1) since it is simple comparisons.
