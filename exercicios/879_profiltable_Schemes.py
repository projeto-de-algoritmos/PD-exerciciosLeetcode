class Solution(object):
 def profitableSchemes(self,n, minProfit, group, profit):
    MOD = 10**9 + 7
    m = len(group)
    
    # Create a 2D array dp to store the number of schemes
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    
    # Initialize the base case
    dp[0][0] = 1
    
    # Iterate over each crime
    for i in range(m):
        members = group[i]
        earn = profit[i]
        
        # Iterate from n to members (backward)
        for j in range(n, members - 1, -1):
            # Iterate from minProfit to 0 (backward)
            for k in range(minProfit, -1, -1):
                # Update the number of schemes
                dp[j][k] = (dp[j][k] + dp[j - members][max(0, k - earn)]) % MOD
    
    # Sum up the number of schemes for different numbers of participants
    total_schemes = 0
    for i in range(n + 1):
        total_schemes = (total_schemes + dp[i][minProfit]) % MOD
    
    return total_schemes