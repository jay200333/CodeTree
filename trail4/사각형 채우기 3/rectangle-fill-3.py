n = int(input())
MOD = 1_000_000_007
dp = [0] * (n+1)

if n == 0:
    print(1)
elif n == 1:
    print(2)
else:
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % MOD
        for j in range(i - 3, -1, -1):
            dp[i] = (dp[i] + dp[j] * 2) % MOD
    print(dp[n])