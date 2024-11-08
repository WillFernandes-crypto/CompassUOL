import datetime as date  # Importa o módulo datetime e o renomeia como date para facilitar a utilização
from block import Block  # Importa a classe Block de outro arquivo chamado block.py

# Gerenciador de toda a estrutura de blocos na blockchain
class Blockchain:
    def __init__(self):
        # Inicializa a cadeia com o bloco gênesis (primeiro bloco da blockchain)
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Cria o bloco gênesis com índice 0, timestamp atual, dados 'Genesis Block' e hash anterior '0'
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    def add_block(self, new_block):
        # Adiciona um novo bloco à cadeia
        
        # Define o hash do bloco anterior como o hash do último bloco na cadeia
        new_block.prev_hash = self.chain[-1].hash
        
        # Calcula o hash do novo bloco
        new_block.hash = new_block.calculate_hash()
        
        # Adiciona o novo bloco à cadeia
        self.chain.append(new_block)

    def add_transaction(self, transaction_data):
        # Adiciona uma nova transação à blockchain
        
        # O índice do novo bloco é igual ao comprimento atual da cadeia
        index = len(self.chain)
        
        # Obtém o timestamp atual
        timestamp = date.datetime.now()
        
        # Cria um novo bloco com os dados da transação e o hash do bloco anterior
        new_block = Block(index, timestamp, transaction_data, self.chain[-1].hash)
        
        # Adiciona o novo bloco à blockchain
        self.add_block(new_block)

    def is_valid(self):
        # Valida a integridade da blockchain
        
        # Percorre todos os blocos, começando do segundo (índice 1)
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]  # Bloco atual
            prev_block = self.chain[i-1]  # Bloco anterior
            
            # Verifica se o hash do bloco atual é igual ao hash calculado
            if current_block.hash != current_block.calculate_hash():
                return False  # Retorna falso se os hashes não corresponderem
            
            # Verifica se o hash anterior do bloco atual é igual ao hash do bloco anterior
            if current_block.prev_hash != prev_block.hash:
                return False  # Retorna falso se o hash anterior não corresponder
        
        # Retorna verdadeiro se todos os blocos passaram nas verificações
        return True
