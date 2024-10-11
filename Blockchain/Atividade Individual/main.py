# Importa a classe Node do módulo node, que representa um nó na rede blockchain
from node import Node
# Importa a classe Network e a função print_blockchain do módulo network
from network import Network, print_blockchain

# Exemplo de uso
# Cria uma instância do nó local com o hostname 'localhost'
my_node = Node("localhost")
# Cria uma instância da rede, passando o nó criado
network = Network(my_node)
# O nó se junta à rede, inicializando a blockchain e anunciando sua presença a outros nós
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
# Chama o método add_transaction da blockchain associada ao nó,
# adicionando a transação de compra ao blockchain
network.blockchain_memory.add_transaction(compra1)
# Chama novamente o método add_transaction para adicionar a transação do documento
network.blockchain_memory.add_transaction(doc)

# Imprimindo a blockchain após as transações
# Chama a função print_blockchain para exibir todos os blocos na cadeia,
# mostrando detalhes como índice, timestamp, dados e hashes
print_blockchain(network.blockchain_memory.chain)
