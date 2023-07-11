class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Inicializa a lista de DP com um valor máximo inicialmente
        dp = [amount + 1] * (amount + 1)
        
        # Define o valor base
        dp[0] = 0
        
        # Preenche a lista de DP usando a abordagem bottom-up
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    # Calcula o número mínimo de moedas necessárias
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Verifica se é possível obter o valor alvo
        if dp[amount] > amount:
            return -1  # Não é possível obter o valor alvo
        else:
            return dp[amount]  # Retorna o número mínimo de moedas necessárias
