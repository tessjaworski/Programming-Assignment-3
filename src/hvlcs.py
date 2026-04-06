def hvlcs(values, A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+ 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = max(dp[i-1][j-1] + values[A[i-1]],
                              dp[i-1][j],
                              dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    max_val = dp[m][n]
    ans = []
    while m > 0 and n > 0:
        if A[m-1] == B[n-1] and dp[m][n] == dp[m-1][n-1] + values[A[m-1]]:
            ans.append(A[m-1])
            m-=1
            n-=1
        elif dp[m][n] == dp[m-1][n]:
            m-=1
        else:
            n-=1

    return max_val, ''.join(reversed(ans))
