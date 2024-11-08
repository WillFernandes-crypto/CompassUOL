> # Atividade Individual
> Desenvolver uma "rede blockchain" com funcionalidades básicas.
> 
> O sistema deve permitir:
> 
> - A criação de transações;
> - A inclusão delas em blocos;
> - A inserção desses blocos na rede;
> - A validação da autenticidade.
> 
> O resultado dessas operações deve ser exportado por meio de logs no console.
> 
> Além disso, o projeto deve garantir a integridade e validação da rede como um todo. A avaliação será estritamente técnica. 
> 
> Não se esqueça de incluir uma documentação detalhada que explique como executar o projeto.
>
> Observações:
> - Criar uma lista encadeada de hashes;

# Ferramentas Utilizadas

## Pré-requisitos
⚠️ Python 3.12

## Configuração Inicial
Para utilizar a aplicação, clone o repositório remoto para a sua máquina local. Isso pode ser feito através do comando:

`git clone https://github.com/WillFernandes-crypto/CompassUOL/tree/main/Blockchain`

## Executando a aplicação
Para executar a aplicação, use o seguinte comando:

`python -u '.\Atividade Individual\main.py'`

## Referências
Os seguintes links serviram de referência para a construção dessa aplicação:
## Recursos

- [Create your own blockchain using Python](https://gruyaume.medium.com/create-your-own-blockchain-using-python-d1250733ce5e)
- [Vídeo: Como criar uma blockchain em Python](https://www.youtube.com/watch?v=yBuzx8akAd0&ab_channel=DataLead)


---
---
---

# Funcionamento do Código

## Importações
- **`import hashlib`**: Importa a biblioteca hashlib, que fornece funções para criar hashes criptográficos.

## Classe Block
- **`class Block:`**: Classe responsável por criar cada um dos blocos na blockchain.
  - **`__init__(self, index, timestamp, data, prev_hash):`**: Construtor da classe Block, que inicializa um novo bloco.
    - **`index`**: Numeração do bloco na cadeia (ex.: 0, 1, 2...).
    - **`timestamp`**: Data e hora em que o bloco foi criado.
    - **`data`**: Informação a ser armazenada no bloco (contexto).
    - **`prev_hash`**: Hash do bloco anterior na cadeia, que conecta os blocos.
  - **`self.index = index`**: Atribui o índice do bloco.
  - **`self.timestamp = timestamp`**: Atribui a data e hora de criação do bloco.
  - **`self.data = data`**: Atribui a informação armazenada no bloco.
  - **`self.prev_hash = prev_hash`**: Atribui o hash do bloco anterior.
  - **`self.hash = self.calculate_hash()`**: Calcula o hash do bloco atual chamando a função `calculate_hash`.
  
  - **`def calculate_hash(self):`**: Método para calcular o hash do bloco atual.
    - **`sha = hashlib.sha256()`**: Cria uma nova instância do algoritmo SHA-256 para gerar o hash.
    - **`sha.update(...)`**: Atualiza a instância SHA-256 com a concatenação dos atributos do bloco (index, timestamp, data e prev_hash).
    - **`return sha.hexdigest()`**: Retorna o hash calculado em formato hexadecimal.

## Classe Blockchain
- **`import datetime as date`**: Importa o módulo datetime e o renomeia como date para facilitar a utilização.
- **`from block import Block`**: Importa a classe Block de outro arquivo chamado block.py.
  
- **`class Blockchain:`**: Gerenciador de toda a estrutura de blocos na blockchain.
  - **`def __init__(self):`**: Inicializa a cadeia com o bloco gênesis (primeiro bloco da blockchain).
    - **`self.chain = [self.create_genesis_block()]`**: Cria a lista de blocos e adiciona o bloco gênesis.
  
  - **`def create_genesis_block(self):`**: Cria o bloco gênesis.
    - **`return Block(0, date.datetime.now(), 'Genesis Block', '0')`**: Retorna um novo bloco com índice 0, timestamp atual, dados 'Genesis Block' e hash anterior '0'.

  - **`def add_block(self, new_block):`**: Adiciona um novo bloco à cadeia.
    - **`new_block.prev_hash = self.chain[-1].hash`**: Define o hash do bloco anterior como o hash do último bloco na cadeia.
    - **`new_block.hash = new_block.calculate_hash()`**: Calcula o hash do novo bloco.
    - **`self.chain.append(new_block)`**: Adiciona o novo bloco à cadeia.

  - **`def add_transaction(self, transaction_data):`**: Adiciona uma nova transação à blockchain.
    - **`index = len(self.chain)`**: O índice do novo bloco é igual ao comprimento atual da cadeia.
    - **`timestamp = date.datetime.now()`**: Obtém o timestamp atual.
    - **`new_block = Block(index, timestamp, transaction_data, self.chain[-1].hash)`**: Cria um novo bloco com os dados da transação e o hash do bloco anterior.
    - **`self.add_block(new_block)`**: Adiciona o novo bloco à blockchain.

  - **`def is_valid(self):`**: Valida a integridade da blockchain.
    - **`for i in range(1, len(self.chain)):`**: Percorre todos os blocos, começando do segundo (índice 1).
    - **`current_block = self.chain[i]`**: Bloco atual.
    - **`prev_block = self.chain[i-1]`**: Bloco anterior.
    - **`if current_block.hash != current_block.calculate_hash():`**: Verifica se o hash do bloco atual é igual ao hash calculado.
      - **`return False`**: Retorna falso se os hashes não corresponderem.
    - **`if current_block.prev_hash != prev_block.hash:`**: Verifica se o hash anterior do bloco atual é igual ao hash do bloco anterior.
      - **`return False`**: Retorna falso se o hash anterior não corresponder.
    - **`return True`**: Retorna verdadeiro se todos os blocos passaram nas verificações.

## Classe Network
- **`import logging`**: Importa o módulo de logging para registrar informações e erros.
- **`import requests`**: Importa o módulo requests para realizar requisições HTTP.
- **`from node import Node, KnownNodesMemory`**: Importa as classes Node e KnownNodesMemory do módulo node.
- **`from blockchain import Blockchain`**: Importa a classe Blockchain do módulo blockchain.

- **`class Network:`**: Classe que gerencia a rede de nós.
  - **`FIRST_KNOWN_NODE_HOSTNAME = "node00.my-blockchain.willhost.com"`**: Define o hostname do nó conhecido padrão da rede.

  - **`def __init__(self, node: Node, init_known_nodes_file: bool = True):`**: Inicializa uma instância da classe Network.
    - **`self.node = node`**: Armazena a instância do nó atual.
    - **`self.blockchain_memory = Blockchain()`**: Cria uma nova instância de Blockchain para armazenar a blockchain local.
    - **`self.known_nodes_memory = KnownNodesMemory()`**: Cria uma nova instância para gerenciar nós conhecidos.
    - **`if init_known_nodes_file:`**: Se `init_known_nodes_file` for verdadeiro, inicializa o arquivo de nós conhecidos.

  - **`def initialize_known_nodes_file(self):`**: Inicializa a lista de nós conhecidos com o nó padrão.
    - **`logging.info("Initializing known nodes file")`**: Registra a inicialização do arquivo de nós conhecidos.
    - **`initial_known_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)`**: Cria um nó inicial com o hostname padrão.
    - **`if self.node.hostname != initial_known_node.hostname:`**: Verifica se o hostname do nó atual é diferente do nó padrão.
      - **`self.known_nodes_memory.store_known_nodes([self.node, initial_known_node])`**: Armazena o nó atual e o nó padrão na memória de nós conhecidos.
    - **`else:`**: Se for o mesmo nó, apenas armazena o nó atual.
      - **`self.known_nodes_memory.store_known_nodes([self.node])`**: Armazena o nó atual.

  - **`def advertise_to_all_known_nodes(self):`**: Método para anunciar o nó atual para todos os nós conhecidos.
    - **`logging.info("Advertising to all known nodes")`**: Registra que está anunciando para todos os nós.
    - **`for known_node in self.known_nodes_memory.return_known_nodes():`**: Itera sobre todos os nós conhecidos.
      - **`if known_node.hostname != self.node.hostname:`**: Verifica se o nó conhecido não é o nó atual.
        - **`try:`**: Tenta anunciar o nó atual para o nó conhecido.
          - **`known_node.advertise(self.node.hostname)`**: Realiza o anúncio.
        - **`except requests.exceptions.ConnectionError:`**: Registra que o nó conhecido não está respondendo.
          - **`logging.info(f"Node not answering: {known_node.hostname}")`**: Registra que o nó conhecido não respondeu.

  - **`def advertise_to_default_node(self):`**: Método para anunciar o nó atual ao nó padrão.
    - **`logging.info("Advertising to default node")`**: Registra que está anunciando ao nó padrão.
    - **`default_node = Node(hostname=self.FIRST_KNOWN_NODE_HOSTNAME)`**: Cria uma instância do nó padrão.
    - **`try:`**: Tenta anunciar o nó atual ao nó padrão.
      - **`default_node.advertise(self.node.hostname)`**: Realiza o anúncio.
      - **`return True`**: Retorna verdadeiro se o anúncio for bem-sucedido.
    - **`except requests.exceptions.ConnectionError:`**: Registra que o nó padrão não está respondendo.
      - **`logging.info(f"Default node not answering: {default_node.hostname}")`**: Registra a falha.
      - **`return False`**: Retorna falso se não for possível se conectar.

  - **`def ask_known_nodes_for_their_known_nodes(self) -> list:`**: Método para solicitar aos nós conhecidos suas próprias listas de nós.
    - **`logging.info("Asking known nodes for their own known nodes")`**: Registra a solicitação de nós conhecidos.
    - **`known_nodes_of_known_nodes = []`**: Inicializa uma lista para armazenar os nós conhecidos recebidos.
    - **`for known_node in self.known_nodes_memory.return_known_nodes():`**: Itera sobre os nós conhecidos.
      - **`if known_node.hostname != self.node.hostname:`**: Verifica se o nó conhecido não é o nó atual.
        - **`try:`**: Tenta solicitar a lista de nós conhecidos ao nó conhecido.
          - **`response = known_node.ask_for_known_nodes()`**: Solicita a lista de nós conhecidos.
          - **`if response:`**: Se houver uma resposta.
            - **`known_nodes_of_known_nodes += response`**: Adiciona os nós conhecidos recebidos à lista.
        - **`except requests.exceptions.ConnectionError:`**: Registra que o nó conhecido não está respondendo.
          - **`logging.info(f"Node not answering: {known_node.hostname}")`**: Registra a falha de conexão.
    - **`return known_nodes_of_known_nodes`**: Retorna a lista de nós conhecidos recebidos.

  - **`def ask_for_the_latest_block(self, known_node: Node) -> dict:`**: Solicita o bloco mais recente a um nó conhecido.
    - **`logging.info(f"Asking for the latest block to {known_node.hostname}")`**: Registra a solicitação do bloco mais recente.
    - **`try:`**: Tenta solicitar o bloco mais recente.
      - **`latest_block = known_node.ask_for_latest_block()`**: Realiza a solicitação.
      - **`if latest_block:`**: Se houver uma resposta.
        - **`logging.info(f"Received latest block from {known_node.hostname}")`**: Registra a recepção do bloco mais recente.
        - **`return latest_block`**: Retorna o bloco mais recente recebido.
    - **`except requests.exceptions.ConnectionError:`**: Registra a falha de conexão.
      - **`logging.info(f"Node not answering: {known_node.hostname}")`**: Registra a falha.

  - **`def add_block_to_memory(self, block: dict):`**: Adiciona um bloco recebido à memória local.
    - **`self.blockchain_memory.add_block(Block(...))`**: Adiciona o bloco à blockchain local, utilizando o dicionário recebido.
  
  - **`def is_valid_block(self, block: dict):`**: Verifica se um bloco é válido.
    - **`return self.blockchain_memory.is_valid()`**: Retorna o resultado da validação da blockchain.

## Notas Adicionais
- A estrutura de classes permite modularidade e reutilização do código.
- A utilização do hashing assegura a integridade dos dados.
- A comunicação entre nós é realizada via requisições HTTP, permitindo a descentralização da rede.


---
---
---
# Recaptulando Blockchains

## O que é um hash?
Funciona como uma "impressão digital" de um determinado dado, de uma quantidade de caracteres ou bytes.

_A partir do hash não é possível gerar o código original._

## O que é um bloco
É uma quantidade de dados agrupado, com tamanho limitado de 1MB no protocolo de bitcoins.

| Bloco                                     |
|-------------------------------------------|
| Número do bloco (altura do bloco no protocolo bitcoin) |
| Nounce                                    |
| Dados                                     |

_Um bloco é considerado minerado toda vez que o minerador encontrar um nounce que faz com que o hash comece com uma certa quantidade de zeros_

## O que é um blockckain
São vários blocos encadeados.

_Na blockchain, o bloco atual possui um novo campo prev, que aponta para o hash do bloco anterior._

| Bloco                                     |
|-------------------------------------------|
| Número do bloco (altura do bloco no protocolo bitcoin) |
| Nounce                                    |
| Dados                                     |
| Hash                                      |
| Hash Prev                                 |
