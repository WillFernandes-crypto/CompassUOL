import hashlib

class Block:
    def __init__(self, index, timestamp, data, prev_hash, reward=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0  # Inicialize o nonce em 0
        self.reward = reward  # Adiciona a recompensa ao bloco
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        # Inclui o nonce no cálculo do hash
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.prev_hash).encode('utf-8') +
            str(self.nonce).encode('utf-8')  # Inclua o nonce aqui
        )
        return sha.hexdigest()
    
    # Método para minerar o bloco com base na dificuldade
    def mine_block(self, difficulty):
        target = '0' * difficulty  # Define o alvo: um hash que começa com um número específico de zeros
        while self.hash[:difficulty] != target:
            self.nonce += 1  # Incrementa o nonce até que o hash corresponda ao alvo
            self.hash = self.calculate_hash()
        print(f"Bloco minerado com sucesso! Nonce: {self.nonce}, Hash: {self.hash}")