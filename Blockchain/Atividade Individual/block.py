import hashlib  # Importa a biblioteca hashlib, que fornece funções para criar hashes criptográficos.

# Classe responsável por criar cada um dos blocos
class Block:
    # Construtor da classe Block, que inicializa um novo bloco.
    # index: numeração do bloco na cadeia (ex.: 0, 1, 2...)
    # timestamp: data e hora em que o bloco foi criado.
    # data: informação a ser armazenada no bloco (contexto).
    # prev_hash: hash do bloco anterior na cadeia, que conecta os blocos.
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index  # Atribui o índice do bloco.
        self.timestamp = timestamp  # Atribui a data e hora de criação do bloco.
        self.data = data  # Atribui a informação armazenada no bloco.
        self.prev_hash = prev_hash  # Atribui o hash do bloco anterior.
        self.hash = self.calculate_hash()  # Calcula o hash do bloco atual chamando a função calculate_hash.

    # Método para calcular o hash do bloco atual.
    def calculate_hash(self):
        sha = hashlib.sha256()  # Cria uma nova instância do algoritmo SHA-256 para gerar o hash.
        # Atualiza a instância SHA-256 com a concatenação dos atributos do bloco (index, timestamp, data e prev_hash)
        sha.update(str(self.index).encode('utf-8') +  # Converte o índice do bloco em bytes e atualiza o hash.
                   str(self.timestamp).encode('utf-8') +  # Converte o timestamp em bytes e atualiza o hash.
                   str(self.data).encode('utf-8') +  # Converte os dados do bloco em bytes e atualiza o hash.
                   str(self.prev_hash).encode('utf-8'))  # Converte o hash do bloco anterior em bytes e atualiza o hash.
        # Retorna o hash calculado em formato hexadecimal.
        return sha.hexdigest()
