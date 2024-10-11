import hashlib
import datetime as date

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
        self.hash = self.calculate_hash() # hash do bloco que está sendo criado

    # Função para calcular o hash
    def calculate_hash(self):
        sha = hashlib.sha256() # função sha256 cria uma variável binária
        # Atualiza a instância que está sendo carregada na variável sha
        # O objetivo é criar de fato o hash
        # Isso acontece concatenando as strings abaixo, no formato utf-8
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.prev_hash).encode('utf-8'))
        # Converte o sha que está em binário para hexadeximal
        return sha.hexdigest()

# Gerenciador de toda a esturutura de blocos na blockchain
class Blockchain:

    # Inicializando o Bloco Gênesis (primeioro bloco da blockchain)
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
        # Captura o último hash salvo na cadeia e imediatamente salva como hash anteiror
        new_block.prev_hash = self.chain[-1].hash
        # Cria o hash para o bloco atual
        new_block.hash = new_block.calculate_hash()
        # Adiciona o novo bloco na blockchain
        self.chain.append(new_block)

    # Função de validação do bloco
    def is_valid(self):

        # Laço de repetição que percorre a cadeia
        # Valida cada um dos blocos na cadeia
        for i in range(1, len(self.chain)):
            current_block = self.chain[i] # bloco atual
            prev_block = self.chain[i-1] # bloco anterior

            # Se o hash do bloco atual for diferente do hash do bloco atual que está sendo gerado
            # Retorna falso
            if current_block.hash != current_block.calculate_hash():
                return False
            # Se o hash anterior do bloco atual for diferente do hash do bloco anterior
            # Retorna falso
            if current_block.prev_hash != prev_block.hash:
                return False
            
            # Senão, retorta verdadeiro
            return True

# Instancia a blockchain criando o bloco gênesis
my_blockchain = Blockchain()

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

# Adiciona um novo bloco com a compra1 à blockchain
my_blockchain.add_block(Block(1, date.datetime.now(), compra1, my_blockchain.chain[-1].hash))

# Adiciona um segundo bloco com o documento à blockchain
my_blockchain.add_block(Block(2,date.datetime.now(), doc, my_blockchain.chain[-1].hash))

# Verifica se a blockchain criada é válida e imprime o resultado
print(f'Is valid blockchain? {str(my_blockchain.is_valid())}')

# Exibe o conteúdo da blockchain (apenas a referência da lista será impressa aqui)
print(my_blockchain)


# Função responsável por imprimir os detalhes de cada bloco na blockchain
def print_blockchain(chain):
    # Laço que percorre cada bloco na cadeia de blocos
    for block in chain:
        print(f'Block: {block.index}') # Imprime o índice do bloco
        print(f'Timestamp: {block.timestamp}') # Imprime a data e hora de criação do bloco
        print(f'Dados: {block.data}') # Imprime os dados armazenados no bloco (como uma transação)
        print(f'Hash: {block.hash}') # Imprime o hash do bloco
        print(f'Hash Prev: {block.prev_hash}') # Imprime o hash do bloco anterior
        print(20*'---') # Separador para facilitar a visualização dos blocos

# Chama a função para imprimir os detalhes da blockchain
print(print_blockchain(my_blockchain.chain))