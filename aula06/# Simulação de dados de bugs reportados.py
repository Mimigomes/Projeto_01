# Simulando dados de vendas diárias
vendas = [
    ('Produto A', 200),
    ('Produto A', 250),
    ('Produto B', 400),
    ('Produto B', 380),
    ('Produto C', 150),
    ('Produto C', 150),
    ('Produto D', 100),
    ('Produto D', 120)
]

# Inicializando dicionário para armazenar total e contagem
resultado = {}

# Processando os dados
for produto, venda in vendas:
    if produto not in resultado:
        resultado[produto] = {'total': 0, 'dias': 0}
    resultado[produto]['total'] += venda
    resultado[produto]['dias'] += 1

# Calculando média e exibindo resultados
print("Resultados de Vendas:")
for produto, dados in resultado.items():
    media_vendas = dados['total'] / dados['dias'] if dados['dias'] > 0 else 0
    print(f"{produto} - Total: {dados['total']}, Média: {media_vendas:.2f}")
