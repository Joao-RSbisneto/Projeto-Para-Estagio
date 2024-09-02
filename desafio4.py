# Definir os valores de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o valor total do faturamento
total_faturamento = sum(faturamento.values())

# Calcular e exibir o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    percentuais[estado] = percentual

# Imprimir os resultados
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")