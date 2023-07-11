class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # Cria uma matriz de DP para armazenar os resultados intermediários
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Preenche a primeira linha e a primeira coluna da matriz de DP
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        # Preenche a matriz de DP usando a abordagem bottom-up
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # Se os caracteres são iguais, não é necessário nenhuma operação de edição
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Caso contrário, seleciona a operação com menor custo (inserção, exclusão ou substituição)
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        # Retorna o valor na posição dp[m][n], que representa o número mínimo de operações de edição
        return dp[m][n]
