def inverter_string(s):
    # Inicializa uma string vazia para armazenar a string invertida
    invertida = ""
    
    # Loop através da string original em ordem inversa
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

# Exemplo de uso com entrada definida no código
string_original = "Exemplo de string"
string_invertida = inverter_string(string_original)
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")

# Exemplo de uso com entrada do usuário
entrada_usuario = input("Digite uma string para inverter: ")
string_invertida_usuario = inverter_string(entrada_usuario)
print(f"String invertida: {string_invertida_usuario}")