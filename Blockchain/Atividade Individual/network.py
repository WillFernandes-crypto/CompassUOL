import logging
import requests
from node import Node, KnownNodesMemory
from blockchain import Blockchain

class Network:
    FIRST_KNOWN_NODE_HOSTNAME = "node00.my-blockchain.willhost.com"

    def __init__(self, node: Node, init_known_nodes_file: bool = True):
        self.node = node
        self.blockchain_memory = Blockchain()
        self.known_nodes_memory = KnownNodesMemory()
        if init_known_nodes_file:
            self.initialize_known_nodes_file()

    def initialize_known_nodes_file(self):
        logging.info("Initializing known nodes file")
        initial_known_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)
        if self.node.hostname != initial_known_node.hostname:
            self.known_nodes_memory.store_known_nodes([self.node, initial_known_node])
        else:
            self.known_nodes_memory.store_known_nodes([self.node])

    def advertise_to_all_known_nodes(self):
        logging.info("Advertising to all known nodes")
        for known_node in self.known_nodes_memory.return_known_nodes():
            if known_node.hostname != self.node.hostname:
                try:
                    known_node.advertise(self.node.hostname)
                except requests.exceptions.ConnectionError:
                    logging.info(f"Node not answering: {known_node.hostname}")

    def advertise_to_default_node(self):
        logging.info("Advertising to default node")
        default_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)
        try:
            default_node.advertise(self.node.hostname)
            return True
        except requests.exceptions.ConnectionError:
            logging.info(f"Default node not answering: {default_node.hostname}")
            return False

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

    def get_longest_blockchain(self):
        logging.info("Retrieving the longest blockchain")
        longest_blockchain_size = 0
        longest_blockchain = self.blockchain_memory.chain
        for node in self.known_nodes_memory.return_known_nodes():
            if isinstance(node, Node):
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

    def initialize_blockchain(self):
        longest_blockchain = self.get_longest_blockchain()
        if longest_blockchain is not None:
            self.blockchain_memory.chain = longest_blockchain
        else:
            self.blockchain_memory.chain = [self.blockchain_memory.create_genesis_block()]

    @property
    def other_nodes_exist(self) -> bool:
        return len(self.known_nodes_memory.return_known_nodes()) > 1

    def join_network(self):
        logging.info("Joining network")
        if self.other_nodes_exist:
            if self.advertise_to_default_node():
                known_nodes_of_known_node = self.ask_known_nodes_for_their_known_nodes()
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

    def return_known_nodes(self):
        return self.known_nodes_memory.return_known_nodes()

# Função responsável por imprimir os detalhes de cada bloco na blockchain
def print_blockchain(chain):
    if chain:
        for block in chain:
            print(f'Block: {block.index}')
            print(f'Timestamp: {block.timestamp}')
            print(f'Data: {block.data}')
            print(f'Hash: {block.hash}')
            print(f'Hash Prev: {block.prev_hash}')
            print(20 * '---')
    else:
        print("The blockchain is empty.")
