import sys

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
    
    # save the max value
    max_val = dp[m][n]
    ans = []

    # get the subsequence
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


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f if line.strip()]

    alphabet_size = int(lines[0])
    values = {}
    for i in range(1, alphabet_size + 1):
        parts = lines[i].split()
        char = parts[0]
        val = int(parts[1])
        values[char] = val

    A,B = lines[alphabet_size+1], lines[alphabet_size+2]

    max_value, subsequence = hvlcs(values,A,B)
    print(max_value)
    print(subsequence)