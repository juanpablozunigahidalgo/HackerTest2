def getExpressionSums(num):
    MOD = 10**9 + 7
    n = len(num)

    # first digit initialisation
    cnt = 1                     # number of expressions so far
    ans = 0                     # sum of finalized parts
    last = int(num[0])          # sum of last terms

    for i in range(1, n):
        d = int(num[i])

        ans = (2 * ans + last) % MOD
        last = (10 * last + 2 * cnt * d) % MOD
        cnt = (2 * cnt) % MOD

    return (ans + last) % MOD
