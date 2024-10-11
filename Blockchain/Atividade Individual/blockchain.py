import hashlib
import datetime as date
import logging
import requests

# Classe responsável por criar cada um dos blocos
class Block:
    # index: numeração do bloco
    # timestamp: data em que o bloco foi criado
    # data: informação a ser armazenada no bloco (contexto)
    # prev_hash: hash do bloco anterior
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()  # hash do bloco que está sendo criado

    # Função para calcular o hash
    def calculate_hash(self):
        sha = hashlib.sha256()  # função sha256 cria uma variável binária
        # Atualiza a instância que está sendo carregada na variável sha
        # O objetivo é criar de fato o hash
        # Isso acontece concatenando as strings abaixo, no formato utf-8
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.prev_hash).encode('utf-8'))
        # Converte o sha que está em binário para hexadeximal
        return sha.hexdigest()

# Gerenciador de toda a estrutura de blocos na blockchain
class Blockchain:
    # Inicializando o Bloco Gênesis (primeiro bloco da blockchain)
    def __init__(self):
        # Define uma cadeia como um vetor, o qual possui o bloco gênesis como o primeiro índice
        self.chain = [self.create_genesis_block()]

    # Criação do primeiro bloco da blockchain
    def create_genesis_block(self):
        # Retorna chamando a classe Block
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    # Adição de um novo bloco na blockchain
    def add_block(self, new_block):
        # Verifica o hash anterior
        # Captura o último hash salvo na cadeia e imediatamente salva como hash anterior
        new_block.prev_hash = self.chain[-1].hash
        # Cria o hash para o bloco atual
        new_block.hash = new_block.calculate_hash()
        # Adiciona o novo bloco na blockchain
        self.chain.append(new_block)

    # Função para adicionar uma transação
    def add_transaction(self, transaction_data):
        index = len(self.chain)  # O índice do novo bloco será o tamanho atual da cadeia
        timestamp = date.datetime.now()
        new_block = Block(index, timestamp, transaction_data, self.chain[-1].hash)
        self.add_block(new_block)

    # Função de validação do bloco
    def is_valid(self):
        # Laço de repetição que percorre a cadeia
        # Valida cada um dos blocos na cadeia
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]  # bloco atual
            prev_block = self.chain[i-1]  # bloco anterior

            # Se o hash do bloco atual for diferente do hash do bloco atual que está sendo gerado
            # Retorna falso
            if current_block.hash != current_block.calculate_hash():
                return False
            # Se o hash anterior do bloco atual for diferente do hash do bloco anterior
            # Retorna falso
            if current_block.prev_hash != prev_block.hash:
                return False

        # Caso passe em todas as verificações, retorna verdadeiro
        return True
class Node:
    # Representação de um nó da rede, com hostname e blockchain
    def __init__(self, hostname):
        self.hostname = hostname
        self.blockchain = Blockchain()

    # Simula a resposta de um nó quando ele é solicitado para enviar sua blockchain
    def get_blockchain(self):
        return self.blockchain.chain

    # Simula a ação de um nó anunciar sua presença para outros nós
    def advertise(self, other_node_hostname):
        logging.info(f'Node {self.hostname} advertised to {other_node_hostname}')
class KnownNodesMemory:
    # Armazena a lista de nós conhecidos na rede
    def __init__(self):
        self.known_nodes = []

    # Armazena a lista de nós conhecidos
    def store_known_nodes(self, nodes):
        self.known_nodes = nodes

    # Retorna os nós conhecidos
    def return_known_nodes(self):
        return self.known_nodes
class Network:
    # Configuração inicial de um nó na rede blockchain
    FIRST_KNOWN_NODE_HOSTNAME = "node00.my-blockchain.gruyaume.com"

    def __init__(self, node: Node, init_known_nodes_file: bool = True):
        self.node = node
        self.blockchain_memory = Blockchain()
        self.known_nodes_memory = KnownNodesMemory()
        if init_known_nodes_file:
            self.initialize_known_nodes_file()

    # Inicializa o arquivo de nós conhecidos com o nó padrão da rede
    def initialize_known_nodes_file(self):
        logging.info("Initializing known nodes file")
        initial_known_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)
        if self.node.hostname != initial_known_node.hostname:
            self.known_nodes_memory.store_known_nodes([self.node, initial_known_node])
        else:
            self.known_nodes_memory.store_known_nodes([self.node])

    # Simula o anúncio do nó atual para os nós conhecidos
    def advertise_to_all_known_nodes(self):
        logging.info("Advertising to all known nodes")
        for known_node in self.known_nodes_memory.return_known_nodes():
            if known_node.hostname != self.node.hostname:
                try:
                    known_node.advertise(self.node.hostname)
                except requests.exceptions.ConnectionError:
                    logging.info(f"Node not answering: {known_node.hostname}")

    # Tenta anunciar o nó atual ao nó padrão da rede
    def advertise_to_all_known_nodes(self):
        logging.info("Advertising to all known nodes")
        for known_node in self.known_nodes_memory.return_known_nodes():
            if isinstance(known_node, Node):  # Verifica se é uma instância da classe Node
                if known_node.hostname != self.node.hostname:
                    try:
                        known_node.advertise(self.node.hostname)
                    except requests.exceptions.ConnectionError:
                        logging.info(f"Node not answering: {known_node.hostname}")
            else:
                logging.error("Known node is not a Node instance")

    def advertise_to_default_node(self):
        logging.info("Advertising to default node")
        default_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)
        try:
            default_node.advertise(self.node.hostname)
            return True  # Se o anúncio for bem-sucedido
        except requests.exceptions.ConnectionError:
            logging.info(f"Default node not answering: {default_node.hostname}")
            return False  # Se não for possível se conectar ao nó padrão

    # Simula a obtenção de nós conhecidos pelos nós atuais
    def ask_known_nodes_for_their_known_nodes(self) -> list:
        logging.info("Asking known nodes for their own known nodes")
        known_nodes_of_known_nodes = []
        for currently_known_node in self.known_nodes_memory.return_known_nodes():
            if currently_known_node.hostname != self.node.hostname:
                try:
                    known_nodes_of_known_node = currently_known_node.get_blockchain()
                    known_nodes_of_known_nodes.extend(known_nodes_of_known_node)
                except requests.exceptions.ConnectionError:
                    logging.info(f"Node not answering: {currently_known_node.hostname}")
        return known_nodes_of_known_nodes

    # Recupera a blockchain mais longa dos nós conhecidos
    def get_longest_blockchain(self):
        logging.info("Retrieving the longest blockchain")
        longest_blockchain_size = 0
        longest_blockchain = self.blockchain_memory.chain  # Corrigido para usar blockchain_memory
        for node in self.known_nodes_memory.return_known_nodes():
            if isinstance(node, Node):  # Verifica se é uma instância da classe Node
                if node.hostname != self.node.hostname:
                    try:
                        blockchain = node.get_blockchain()
                        blockchain_length = len(blockchain)
                        if blockchain_length > longest_blockchain_size:
                            longest_blockchain_size = blockchain_length
                            longest_blockchain = blockchain
                    except requests.exceptions.ConnectionError:
                        logging.info(f"Node not answering: {node.hostname}")
        logging.info(f"Longest blockchain has a size of {longest_blockchain_size} blocks")
        return longest_blockchain
    
    # Inicializa a blockchain do nó
    def initialize_blockchain(self):
        longest_blockchain = self.get_longest_blockchain()
        if longest_blockchain is not None:  # Verifica se a blockchain não é None
            self.blockchain_memory.chain = longest_blockchain  # Corrigido
        else:
            self.blockchain_memory.chain = [self.blockchain_memory.create_genesis_block()]  # Cria a blockchain com o bloco gênesis

    # Verifica se existem outros nós na rede
    @property
    def other_nodes_exist(self) -> bool:
        return len(self.known_nodes_memory.return_known_nodes()) > 1

    # Junta o nó atual à rede
    def join_network(self):
        logging.info("Joining network")
        if self.other_nodes_exist:
            if self.advertise_to_default_node():
                known_nodes_of_known_node = self.ask_known_nodes_for_their_known_nodes()
                # Verifique se os nós conhecidos são do tipo Node antes de armazená-los
                valid_nodes = [node for node in known_nodes_of_known_node if isinstance(node, Node)]
                self.known_nodes_memory.store_known_nodes(valid_nodes)
                self.advertise_to_all_known_nodes()
                self.initialize_blockchain()
            else:
                logging.info("Default node didn't answer. Initializing local blockchain.")
                self.initialize_blockchain()
        else:
            logging.info("No other nodes exist. Initializing as the first node.")
            self.initialize_blockchain()

    # Retorna os nós conhecidos
    def return_known_nodes(self):
        return self.known_nodes_memory.return_known_nodes()

# Função responsável por imprimir os detalhes de cada bloco na blockchain
def print_blockchain(chain):
    if chain:  # Verifica se a cadeia não está vazia
        for block in chain:
            print(f'Block: {block.index}')  # Imprime o índice do bloco
            print(f'Timestamp: {block.timestamp}')  # Imprime a data e hora de criação do bloco
            print(f'Data: {block.data}')  # Imprime os dados armazenados no bloco
            print(f'Hash: {block.hash}')  # Imprime o hash do bloco
            print(f'Hash Prev: {block.prev_hash}')  # Imprime o hash do bloco anterior
            print(20 * '---')  # Separador para facilitar a visualização dos blocos
    else:
        print("The blockchain is empty.")

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
