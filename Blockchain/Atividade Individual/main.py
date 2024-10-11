from node import Node
from network import Network, print_blockchain

# Exemplo de uso
my_node = Node("localhost")
network = Network(my_node)
network.join_network()

# Dicionário que simula uma transação de compra de um item
compra1 = {
    'item': 'Asus ROG',
    'valor': 12,
    'comprador': '@Will',
    'vendedor': '@Asus'
}

# Dicionário que simula uma transação de um documento
doc = {
    'item': 'escritura da casa',
    'valor_pago_ao_cartorio': 3,
    'comprador': '@Will',
    'vendedor': '@Cartorio'
}

# Adicionando as transações à blockchain
network.blockchain_memory.add_transaction(compra1)
network.blockchain_memory.add_transaction(doc)

# Imprimindo a blockchain após as transações
print_blockchain(network.blockchain_memory.chain)
