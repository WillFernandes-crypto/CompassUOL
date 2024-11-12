> # Atividade Individual
> Incrementar a blockchain desenvolvida na Atividade Individual.
> 
> Novas adições realizadas:
> 
> - Sistema de proof of work, com nonce e dificuldade;
> - Determinar a estrutura de um endereço válido (a critério próprio, ex: 2x + 48 caracteres hexadecimais) e garantir que uma transação só aconteça se todos os endereços envolvidos sejam válidos;
> - Histórico de transações por endereço;

# Ferramentas Utilizadas

## Pré-requisitos
⚠️ Python 3.12

## Recomendação de GUI e IDE
[Anaconda](https://www.anaconda.com/download)

Spyder - IDE inclusa no Anaconda.

## Configuração Inicial
Para utilizar a aplicação, clone o repositório remoto para a sua máquina local. Isso pode ser feito através do comando:

`git clone https://github.com/WillFernandes-crypto/CompassUOL/tree/main/Blockchain/Atividade%20Individual%2002`

## Executando a aplicação
Para executar a aplicação, use o seguinte comando:

`python -u '.\Atividade Individual 02\main.py'`

## Referências
Os seguintes links serviram de referência para a construção dessa aplicação:
## Recursos

- [Create your own blockchain using Python](https://gruyaume.medium.com/create-your-own-blockchain-using-python-d1250733ce5e)
- [Vídeo: Como criar uma blockchain em Python](https://www.youtube.com/watch?v=yBuzx8akAd0&ab_channel=DataLead)
- [Implementing the Proof-of-Work Algorithm in Python for Blockchain Mining](https://www.geeksforgeeks.org/implementing-the-proof-of-work-algorithm-in-python-for-blockchain-mining/)
- [Regular Expression (RegEx) in Python with Examples](https://www.geeksforgeeks.org/regular-expression-python-examples/)
- [Build your own blockchain in Python: a practical guide](https://bimoputro.medium.com/build-your-own-blockchain-in-python-a-practical-guide-f9620327ed03)


---
---
---

# Funcionamento do Código

## Arquivo main.py
O arquivo main.py inicia um nó de blockchain, adiciona transações e imprime o estado da blockchain:

### Inicialização do Nó e da Rede:

```
my_node = Node("localhost")
network = Network(my_node)
network.join_network()
```

Um nó é criado com o endereço "localhost", e uma rede é instanciada usando esse nó. Em seguida, o nó é conectado à rede com `join_network()`.

### Adicionando Transações:
Transações são definidas com dados como item, valor, comprador, e vendedor. Essas transações são então adicionadas à memória da blockchain:

```
network.blockchain_memory.add_transaction(compra1)
network.blockchain_memory.add_transaction(doc)
```

### Impressão da Blockchain:
Após adicionar transações, a função `print_blockchain()` exibe todos os blocos presentes na blockchain. A função exibe o índice, o timestamp, os dados, o hash e o hash do bloco anterior.

### Consulta do Histórico de Transações:
Com `consultar_historico_endereco()`, o histórico de transações de um endereço específico pode ser verificado e exibido.

## Arquivo block.py
O arquivo block.py define a classe Block, que representa cada bloco individual na blockchain:

### Inicialização do Bloco:
Cada bloco possui um índice, timestamp, dados da transação, prev_hash (hash do bloco anterior), nonce e hash.

### Cálculo do Hash:
O método `calculate_hash()` gera o hash do bloco usando sha256. Esse método é chamado sempre que o hash é recalculado.

### Mineração do Bloco:
O método `mine_block(difficulty)` ajusta o nonce até que o hash do bloco satisfaça uma dificuldade específica, representada pela quantidade de zeros no início do hash.

### Arquivo blockchain.py
O arquivo blockchain.py define a classe Blockchain, que gerencia a estrutura de blocos e transações.

### Inicialização:
A blockchain começa com um bloco gênesis e define um nível de dificuldade para mineração.

### Adição de Blocos:
O método `add_block()` adiciona um novo bloco à blockchain e realiza a mineração do bloco.

### Adição de Transações:
O método `add_transaction()` verifica a validade dos endereços e do valor da transação antes de adicioná-la em um bloco novo. Transações são registradas no histórico dos endereços envolvidos.

### Validação de Endereços:
O método `is_valid_address()` usa uma expressão regular para validar o comprimento e a estrutura de um endereço (50 caracteres, sendo os dois primeiros letras).

### Histórico de Transações:
O método `get_transaction_history()` retorna as transações associadas a um endereço específico, armazenando-as em um dicionário transaction_history.

## Arquivo network.py
O arquivo network.py implementa a classe Network, que gerencia a conexão e comunicação entre os nós da rede:

### Inicialização da Rede:
A rede é iniciada com um nó padrão conhecido _(FIRST_KNOWN_NODE_HOSTNAME)_.

### Propagação e Publicidade do Nó:
Métodos como `advertise_to_all_known_nodes()` e `advertise_to_default_node()` permitem que o nó atual se anuncie para outros nós conhecidos, facilitando a descoberta de novos nós na rede.

### Obtenção da Blockchain Mais Longa:
O método `get_longest_blockchain()` busca a blockchain mais longa entre todos os nós conhecidos, garantindo que todos os nós mantenham a mesma versão da blockchain.

### Entrada na Rede:
O método `join_network()` gerencia o processo de entrada do nó na rede, incluindo a sincronização de nós conhecidos e a inicialização da blockchain.

## Arquivo node.py
O arquivo node.py define as classes Node e KnownNodesMemory, que representam um nó individual e a memória dos nós conhecidos:

### Classe Node:
Um nó representa uma instância da blockchain e possui um hostname e uma blockchain. O método `get_blockchain()` permite que o nó compartilhe sua cadeia de blocos, enquanto o método `advertise()` permite que ele anuncie sua presença para outros nós.

### Classe KnownNodesMemory:
Esta classe gerencia a lista de nós conhecidos e fornece métodos para armazenar e retornar nós conhecidos na rede.

## Funções Auxiliares
### Função `print_blockchain()`:
Imprime os detalhes de cada bloco na blockchain, usada para visualizar a estrutura da cadeia.

### Função `consultar_historico_endereco()`:
Permite consultar e exibir o histórico de transações de um endereço específico.