import logging
import requests
from blockchain import Blockchain

class Node:
    def __init__(self, hostname):
        self.hostname = hostname
        self.blockchain = Blockchain()

    def get_blockchain(self):
        return self.blockchain.chain

    def advertise(self, other_node_hostname):
        logging.info(f'Node {self.hostname} advertised to {other_node_hostname}')

class KnownNodesMemory:
    def __init__(self):
        self.known_nodes = []

    def store_known_nodes(self, nodes):
        self.known_nodes = nodes

    def return_known_nodes(self):
        return self.known_nodes
