N, K = map(int,input().split())
arr = []
for i in range(N):
    W, V = map(int,input().split())
    arr.append((W,V))
arr.sort(reverse=True)
dp = [0 for _ in range(K+1)]

for W,V in arr:
    for j in range(K,W-1,-1):
        dp[j] = max(dp[j],dp[j-W] + V)

print(max(dp))
