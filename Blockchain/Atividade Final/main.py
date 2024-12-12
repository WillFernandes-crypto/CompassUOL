from node import Node
from network import Network, print_blockchain, consultar_historico_endereco

my_node = Node("localhost")
network = Network(my_node)
network.join_network()

compra1 = {
    'item': 'Asus ROG',  
    'valor': 12,  
    'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',  # 50 caracteres
    'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890'   # 50 caracteres
}

doc = {
    'item': 'escritura da casa',  
    'valor_pago_ao_cartorio': 3, 
    'comprador': 'CC1234567890abcdef1234567890abcdef1234567890abcdef12',  # 52 caracteres
    'vendedor': 'DDabcdef1234567890abcdef1234567890abcdef1234567890ab'   # 52 caracteres
}

# Adicionando as transações à blockchain
network.blockchain_memory.add_transaction(compra1)
# Chama novamente o método add_transaction para adicionar a transação do documento
network.blockchain_memory.add_transaction(doc)

# Imprimindo a blockchain após as transações
print_blockchain(network.blockchain_memory.chain)

# Consultando o histórico de transações de um endereço
endereco_comprador = 'AA1234567890abcdef1234567890abcdef1234567890abcdef'
consultar_historico_endereco(endereco_comprador, network.blockchain_memory)
