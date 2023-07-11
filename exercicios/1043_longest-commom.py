class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        # Cria uma matriz de DP para armazenar os resultados intermediários
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Preenche a matriz de DP usando a abordagem bottom-up
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    # Se os caracteres são iguais, incrementa o comprimento da subsequência
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Caso contrário, seleciona o máximo entre o comprimento das subsequências sem o caractere atual
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Retorna o valor na posição dp[m][n], que representa o comprimento da maior subsequência comum
        return dp[m][n]
