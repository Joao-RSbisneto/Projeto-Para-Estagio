def processar_faturamento(filename):
    # Ler os dados do arquivo JSON
    with open(filename, 'r') as file:
        dados = json.load(file)
    
    # Extrair os valores de faturamento
    faturamento = [item['valor'] for item in dados['faturamento']]
    
    # Filtrar os dias com faturamento
    faturamento_filtrado = [valor for valor in faturamento if valor > 0]
    
    if not faturamento_filtrado:
        return None, None, 0
    
    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)
    
    # Calcular a média mensal de faturamento
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    # Contar o número de dias com faturamento superior à média mensal
    dias_acima_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

# Exemplo de uso
filename = 'faturamento.json'
menor_faturamento, maior_faturamento, dias_acima_media = processar_faturamento(filename)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")