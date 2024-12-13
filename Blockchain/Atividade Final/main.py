from node import Node
from network import Network, print_blockchain, consultar_historico_endereco

my_node = Node("localhost")
network = Network(my_node)
network.join_network()

# Inicializando saldos para os endereços
network.blockchain_memory.balances['AA1234567890abcdef1234567890abcdef1234567890abcdef'] = 100
network.blockchain_memory.balances['CC1234567890abcdef1234567890abcdef1234567890abcdef'] = 100

compra1 = {
    'item': 'Asus ROG',  
    'valor': 12,  
    'taxa': 1,  # Adiciona a taxa de transação
    'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',  # 50 caracteres
    'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890'   # 50 caracteres
}

doc = {
    'item': 'escritura da casa',  
    'valor': 3, 
    'taxa': 0.5,  # Adiciona a taxa de transação
    'comprador': 'CC1234567890abcdef1234567890abcdef1234567890abcdef',  # 50 caracteres
    'vendedor': 'DDabcdef1234567890abcdef1234567890abcdef1234567890'   # 50 caracteres
}

# Adicionando as transações à blockchain
network.blockchain_memory.add_transaction(compra1)
network.propagate_transaction(compra1)  # Propaga a transação para outros nós

network.blockchain_memory.add_transaction(doc)
network.propagate_transaction(doc)  # Propaga a transação para outros nós

# Imprimindo a blockchain após as transações
print_blockchain(network.blockchain_memory.chain)

# Consultando o histórico de transações de um endereço
endereco_comprador = 'AA1234567890abcdef1234567890abcdef1234567890abcdef'
consultar_historico_endereco(endereco_comprador, network.blockchain_memory)

# Imprimindo os saldos dos endereços
print("\nSaldos dos endereços:")
for endereco, saldo in network.blockchain_memory.balances.items():
    print(f"Endereço: {endereco}, Saldo: {saldo}")