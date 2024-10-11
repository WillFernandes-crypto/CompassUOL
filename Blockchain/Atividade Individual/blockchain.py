import datetime as date
from block import Block

# Gerenciador de toda a estrutura de blocos na blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    def add_block(self, new_block):
        new_block.prev_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_transaction(self, transaction_data):
        index = len(self.chain)
        timestamp = date.datetime.now()
        new_block = Block(index, timestamp, transaction_data, self.chain[-1].hash)
        self.add_block(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.prev_hash != prev_block.hash:
                return False
        return True
