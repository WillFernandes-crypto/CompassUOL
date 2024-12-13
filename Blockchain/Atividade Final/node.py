import logging 
from blockchain import Blockchain

# Classe que representa um nó na rede blockchain
class Node:
    # Método construtor que inicializa o nó com um hostname e cria uma nova blockchain
    def __init__(self, hostname):
        self.hostname = hostname  # Atribui o hostname ao nó
        self.blockchain = Blockchain()  # Inicializa a blockchain associada a este nó

    # Método que retorna a cadeia de blocos da blockchain deste nó
    def get_blockchain(self):
        return self.blockchain.chain  # Retorna a lista de blocos (cadeia) da blockchain

    # Método que registra a ação de um nó anunciar sua presença para outro nó
    def advertise(self, other_node_hostname):
        logging.info(f'Node {self.hostname} advertised to {other_node_hostname}') 

    # Método para receber um bloco propagado
    def receive_block(self, block):
        logging.info(f'Node {self.hostname} received block {block.index}')
        self.blockchain.add_block(block)

    # Método para receber uma transação propagada
    def receive_transaction(self, transaction):
        logging.info(f'Node {self.hostname} received transaction')
        self.blockchain.add_transaction(transaction)

# Classe que gerencia a memória dos nós conhecidos na rede
class KnownNodesMemory:
    # Método construtor que inicializa a lista de nós conhecidos
    def __init__(self):
        self.known_nodes = []  # Inicializa a lista como vazia

    # Método que armazena uma lista de nós conhecidos
    def store_known_nodes(self, nodes):
        self.known_nodes = nodes  # Armazena a lista de nós conhecidos na variável conhecida

    # Método que retorna a lista de nós conhecidos
    def return_known_nodes(self):
        return self.known_nodes  # Retorna a lista de nós conhecidos armazenados