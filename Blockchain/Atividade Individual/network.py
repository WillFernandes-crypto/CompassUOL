import logging  # Importa o módulo de logging para registrar informações e erros.
import requests  # Importa o módulo requests para realizar requisições HTTP.
from node import Node, KnownNodesMemory  # Importa as classes Node e KnownNodesMemory do módulo node.
from blockchain import Blockchain  # Importa a classe Blockchain do módulo blockchain.

class Network:
    # Define o hostname do nó conhecido padrão da rede.
    FIRST_KNOWN_NODE_HOSTNAME = "node00.my-blockchain.willhost.com"

    # Método construtor que inicializa uma instância da classe Network.
    def __init__(self, node: Node, init_known_nodes_file: bool = True):
        self.node = node  # Armazena a instância do nó atual.
        self.blockchain_memory = Blockchain()  # Cria uma nova instância de Blockchain para armazenar a blockchain local.
        self.known_nodes_memory = KnownNodesMemory()  # Cria uma nova instância para gerenciar nós conhecidos.
        
        # Se init_known_nodes_file for verdadeiro, inicializa o arquivo de nós conhecidos.
        if init_known_nodes_file:
            self.initialize_known_nodes_file()

    # Inicializa a lista de nós conhecidos com o nó padrão.
    def initialize_known_nodes_file(self):
        logging.info("Initializing known nodes file")  # Registra a inicialização do arquivo de nós conhecidos.
        initial_known_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)  # Cria um nó inicial com o hostname padrão.
        
        # Verifica se o hostname do nó atual é diferente do nó padrão.
        if self.node.hostname != initial_known_node.hostname:
            # Armazena o nó atual e o nó padrão na memória de nós conhecidos.
            self.known_nodes_memory.store_known_nodes([self.node, initial_known_node])
        else:
            # Se for o mesmo nó, apenas armazena o nó atual.
            self.known_nodes_memory.store_known_nodes([self.node])

    # Método para anunciar o nó atual para todos os nós conhecidos.
    def advertise_to_all_known_nodes(self):
        logging.info("Advertising to all known nodes")  # Registra que está anunciando para todos os nós.
        # Itera sobre todos os nós conhecidos.
        for known_node in self.known_nodes_memory.return_known_nodes():
            # Verifica se o nó conhecido não é o nó atual.
            if known_node.hostname != self.node.hostname:
                try:
                    # Tenta anunciar o nó atual para o nó conhecido.
                    known_node.advertise(self.node.hostname)
                except requests.exceptions.ConnectionError:
                    # Registra que o nó conhecido não está respondendo.
                    logging.info(f"Node not answering: {known_node.hostname}")

    # Método para anunciar o nó atual ao nó padrão.
    def advertise_to_default_node(self):
        logging.info("Advertising to default node")  # Registra que está anunciando ao nó padrão.
        default_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)  # Cria uma instância do nó padrão.
        try:
            # Tenta anunciar o nó atual ao nó padrão.
            default_node.advertise(self.node.hostname)
            return True  # Retorna verdadeiro se o anúncio for bem-sucedido.
        except requests.exceptions.ConnectionError:
            # Registra que o nó padrão não está respondendo.
            logging.info(f"Default node not answering: {default_node.hostname}")
            return False  # Retorna falso se não for possível se conectar.

    # Método para solicitar aos nós conhecidos suas próprias listas de nós.
    def ask_known_nodes_for_their_known_nodes(self) -> list:
        logging.info("Asking known nodes for their own known nodes")  # Registra a solicitação de nós conhecidos.
        known_nodes_of_known_nodes = []  # Lista para armazenar nós conhecidos obtidos.
        
        # Itera sobre os nós conhecidos.
        for currently_known_node in self.known_nodes_memory.return_known_nodes():
            # Verifica se o nó conhecido não é o nó atual.
            if currently_known_node.hostname != self.node.hostname:
                try:
                    # Obtém a blockchain do nó conhecido.
                    known_nodes_of_known_node = currently_known_node.get_blockchain()
                    # Adiciona os nós conhecidos à lista.
                    known_nodes_of_known_nodes.extend(known_nodes_of_known_node)
                except requests.exceptions.ConnectionError:
                    # Registra que o nó conhecido não está respondendo.
                    logging.info(f"Node not answering: {currently_known_node.hostname}")
        return known_nodes_of_known_nodes  # Retorna a lista de nós conhecidos.

    # Método para recuperar a blockchain mais longa entre os nós conhecidos.
    def get_longest_blockchain(self):
        logging.info("Retrieving the longest blockchain")  # Registra que está recuperando a blockchain mais longa.
        longest_blockchain_size = 0  # Inicializa a variável para armazenar o tamanho da blockchain mais longa.
        longest_blockchain = self.blockchain_memory.chain  # Inicializa a variável com a blockchain atual.
        
        # Itera sobre os nós conhecidos.
        for node in self.known_nodes_memory.return_known_nodes():
            # Verifica se o objeto é uma instância da classe Node.
            if isinstance(node, Node):
                # Verifica se o nó conhecido não é o nó atual.
                if node.hostname != self.node.hostname:
                    try:
                        # Obtém a blockchain do nó conhecido.
                        blockchain = node.get_blockchain()
                        blockchain_length = len(blockchain)  # Obtém o comprimento da blockchain.
                        
                        # Se a blockchain for mais longa que a armazenada, atualiza as variáveis.
                        if blockchain_length > longest_blockchain_size:
                            longest_blockchain_size = blockchain_length
                            longest_blockchain = blockchain
                    except requests.exceptions.ConnectionError:
                        # Registra que o nó conhecido não está respondendo.
                        logging.info(f"Node not answering: {node.hostname}")
        
        logging.info(f"Longest blockchain has a size of {longest_blockchain_size} blocks")  # Registra o tamanho da blockchain mais longa.
        return longest_blockchain  # Retorna a blockchain mais longa.

    # Método para inicializar a blockchain do nó.
    def initialize_blockchain(self):
        longest_blockchain = self.get_longest_blockchain()  # Obtém a blockchain mais longa.
        
        # Se a blockchain mais longa não for None, inicializa com ela.
        if longest_blockchain is not None:
            self.blockchain_memory.chain = longest_blockchain
        else:
            # Caso contrário, inicializa com o bloco gênesis.
            self.blockchain_memory.chain = [self.blockchain_memory.create_genesis_block()]

    # Propriedade que verifica se existem outros nós na rede.
    @property
    def other_nodes_exist(self) -> bool:
        return len(self.known_nodes_memory.return_known_nodes()) > 1  # Retorna verdadeiro se houver mais de um nó conhecido.

    # Método que permite ao nó atual entrar na rede.
    def join_network(self):
        logging.info("Joining network")  # Registra a tentativa de entrada na rede.
        
        # Verifica se existem outros nós na rede.
        if self.other_nodes_exist:
            if self.advertise_to_default_node():  # Tenta anunciar ao nó padrão.
                known_nodes_of_known_node = self.ask_known_nodes_for_their_known_nodes()  # Solicita os nós conhecidos.
                # Filtra apenas os nós válidos (instâncias da classe Node).
                valid_nodes = [node for node in known_nodes_of_known_node if isinstance(node, Node)]
                self.known_nodes_memory.store_known_nodes(valid_nodes)  # Armazena os nós válidos.
                self.advertise_to_all_known_nodes()  # Anuncia para todos os nós conhecidos.
                self.initialize_blockchain()  # Inicializa a blockchain.
            else:
                logging.info("Default node didn't answer. Initializing local blockchain.")  # Registra se o nó padrão não respondeu.
                self.initialize_blockchain()  # Inicializa a blockchain local.
        else:
            logging.info("No other nodes exist. Initializing as the first node.")  # Registra se não existem outros nós.
            self.initialize_blockchain()  # Inicializa a blockchain como o primeiro nó.

    # Método que retorna os nós conhecidos.
    def return_known_nodes(self):
        return self.known_nodes_memory.return_known_nodes()  # Retorna a lista de nós conhecidos.

# Função responsável por imprimir os detalhes de cada bloco na blockchain.
def print_blockchain(chain):
    if chain:  # Verifica se a cadeia não está vazia.
        for block in chain:
            print(f'Block: {block.index}')  # Imprime o índice do bloco.
            print(f'Timestamp: {block.timestamp}')  # Imprime a data e hora de criação do bloco.
            print(f'Data: {block.data}')  # Imprime os dados armazenados no bloco.
            print(f'Hash: {block.hash}')  # Imprime o hash do bloco.
            print(f'Hash Prev: {block.prev_hash}')  # Imprime o hash do bloco anterior.
            print(20 * '---')  # Imprime um separador para facilitar a visualização.
    else:
        print("The blockchain is empty.")  # Mensagem indicando que a blockchain está vazia.
