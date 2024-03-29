# O(n^2)
N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))