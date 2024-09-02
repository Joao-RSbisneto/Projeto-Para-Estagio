def pertence_fibonacci(numero):
    # Verifica se o número é negativo
    if numero < 0:
        return False
    
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Caso especial para os números 0 e 1
    if numero == a or numero == b:
        return True
    
    # Gera a sequência de Fibonacci até encontrar o número ou ultrapassá-lo
    while b < numero:
        a, b = b, a + b
    
    # Verifica se o número é igual ao último número da sequência gerado
    return b == numero

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Verifica se o número pertence à sequência de Fibonacci e exibe a mensagem correspondente
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")