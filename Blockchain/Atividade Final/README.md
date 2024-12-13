# Atividade Final: Construção de uma Blockchain Básica

## Objetivos
Com esta atividade, vocês vão:
1. Simular uma rede onde diferentes “nós” trocam informações sobre blocos e transações.
2. Aprender a resolver conflitos (forks) e garantir que todos os nós concordem com a mesma cadeia.
3. Implementar um sistema que controla os saldos dos endereços e garante que só transações válidas sejam processadas.
4. Adicionar taxas de transação e recompensas para mineradores.

## O que foi implementado

### 1. Propagação de Blocos e Transações
Imagine que cada nó na rede tem sua própria cópia da blockchain. Quando um novo bloco ou transação é criado, ele precisa ser compartilhado com os outros nós. Essa comunicação é essencial para manter a blockchain sincronizada.
- **Tarefa:** Criar uma função que simula essa troca de informações entre os nós.
- **Funções Implementadas:**
  - `propagate_block` em [`network.py`](Blockchain/Atividade Final/network.py): Propaga um bloco para todos os nós conhecidos.
  - `propagate_transaction` em [`network.py`](Blockchain/Atividade Final/network.py): Propaga uma transação para todos os nós conhecidos.

### 2. Resolução de Conflitos (Forks)
Em uma rede real, às vezes surgem dois blocos “competindo” para serem o próximo na cadeia. Isso gera um fork. Para resolver esse conflito, usamos uma regra simples: a cadeia mais longa vence.
- **Tarefa:** Quando um nó detecta um fork, ele deve:
  1. Comparar as cadeias recebidas.
  2. Adotar a cadeia mais longa como válida.
- **Funções Implementadas:**
  - `get_longest_blockchain` em [`network.py`](Blockchain/Atividade Final/network.py): Recupera a blockchain mais longa entre os nós conhecidos.
  - `initialize_blockchain` em [`network.py`](Blockchain/Atividade Final/network.py): Inicializa a blockchain do nó com a cadeia mais longa.

### 3. Estado Global e Controle de Saldos
Agora é hora de dar mais significado aos endereços que vocês criaram. Cada endereço terá um saldo, e as transações devem obedecer a essa regra básica: ninguém pode gastar mais do que possui.
- **Tarefa:**
  1. Adicionar um sistema para rastrear os saldos de cada endereço.
  2. Atualizar os saldos sempre que um bloco for minerado e incluído na cadeia.
- **Funções Implementadas:**
  - `update_balances` em [`blockchain.py`](Blockchain/Atividade Final/blockchain.py): Atualiza os saldos dos endereços após a mineração de um bloco.
  - `get_transaction_history` em [`blockchain.py`](Blockchain/Atividade Final/blockchain.py): Retorna o histórico de transações de um endereço específico.

### 4. Taxas de Transação e Recompensas
Para tornar a mineração mais interessante, vamos adicionar taxas às transações. Essas taxas serão somadas à recompensa que o minerador já recebe por cada bloco minerado.
- **Tarefa:**
  1. Adicionar um campo taxa às transações.
  2. Modificar a lógica de mineração para somar todas as taxas das transações do bloco à recompensa do minerador.
- **Funções Implementadas:**
  - `add_transaction` em [`blockchain.py`](Blockchain/Atividade Final/blockchain.py): Adiciona uma transação à blockchain, incluindo a taxa.
  - `mine_block` em [`block.py`](Blockchain/Atividade Final/block.py): Minera um bloco com base na dificuldade, incluindo a recompensa e as taxas.

## Ferramentas Utilizadas

### Pré-requisitos
⚠️ Python 3.12

### Recomendação de GUI e IDE
- Anaconda
- Spyder - IDE inclusa no Anaconda.

## Configuração Inicial
Para utilizar a aplicação, clone o repositório remoto para a sua máquina local. Isso pode ser feito através do comando:

```sh
git clone https://github.com/WillFernandes-crypto/CompassUOL/tree/main/Blockchain/Atividade%20Individual%2002
```

## Executando a aplicação
Para executar a aplicação, use o seguinte comando:
```sh
python -u '.\Atividade Individual 02\main.py'
```

## Funcionamento do Código

### Explicação das Funções
`block.py`
- Block **Class:**
  - **calculate_hash:** Calcula o hash do bloco incluindo o nonce.
  - **mine_block:** Minera o bloco ajustando o nonce até que o hash atenda à dificuldade especificada.

`blockchain.py`
- Blockchain **Class:**
  - **create_genesis_block:** Cria o bloco gênesis.
  - **add_transaction:** Adiciona uma transação à mempool, verificando assinaturas e saldos.
  - **mine_pending_transactions:** Minera transações pendentes da mempool e adiciona o bloco à blockchain.
  - **update_balances:** Atualiza os saldos dos endereços após a mineração de um bloco.
  - **get_transaction_history:** Retorna o histórico de transações de um endereço específico.
  - **is_valid_address:** Verifica se um endereço é válido.
  - **verify_signature:** Verifica a assinatura de uma transação.

`network.py`
- Network **Class:**
  - **initialize_known_nodes_file:** Inicializa a lista de nós conhecidos.
  - **advertise_to_all_known_nodes:** Anuncia o nó atual para todos os nós conhecidos.
  - **advertise_to_default_node:** Anuncia o nó atual ao nó padrão.
  - **ask_known_nodes_for_their_known_nodes:** Solicita aos nós conhecidos suas próprias listas de nós.
  - **get_longest_blockchain:** Recupera a blockchain mais longa entre os nós conhecidos.
  - **initialize_blockchain:** Inicializa a blockchain do nó com a cadeia mais longa.
  - **join_network:** Permite ao nó atual entrar na rede.
  - **propagate_block:** Propaga um bloco para todos os nós conhecidos.
  - **propagate_transaction:** Propaga uma transação para todos os nós conhecidos.

`node.py`
- Node **Class:**
  - **get_blockchain:** Retorna a cadeia de blocos da blockchain deste nó.
  - **advertise:** Registra a ação de um nó anunciar sua presença para outro nó.
  - **receive_block:** Recebe um bloco propagado.
  - **receive_transaction:** Recebe uma transação propagada.
- KnownNodesMemory **Class:**
  - **store_known_nodes:** Armazena uma lista de nós conhecidos.
  - **return_known_nodes:** Retorna a lista de nós conhecidos.

## Explicação Detalhada da Saída

1. Verificação de Endereços:
   - O sistema verifica se os endereços dos compradores e vendedores são válidos.
   - Mensagens como "Verificando endereço: aa1234567890abcdef1234567890abcdef1234567890abcdef" indicam que o endereço está sendo verificado.
   - Mensagens como "Endereço válido: 'aa1234567890abcdef1234567890abcdef1234567890abcdef'" confirmam que o endereço é válido.

2. Mineração de Bloco:
   - A mensagem "Bloco minerado com sucesso! Nonce: 176468, Hash: 00003537e6bcd331ae9b7d477720c43bb3a13539045240824cf76f7023fe3284" indica que um bloco foi minerado com sucesso.
   - O nonce é o valor que foi ajustado para encontrar um hash que atenda à dificuldade especificada.

3. Detalhes dos Blocos:
   - **Block 0:** É o bloco gênesis, o primeiro bloco da cadeia.
     - `Timestamp:` Data e hora de criação do bloco.
     - `Data:` "Genesis Block" indica que é o bloco gênesis.
     - `Hash:` Hash do bloco gênesis.
     - `Hash Prev:` Hash do bloco anterior (0 para o bloco gênesis).
   - **Block 1:** Contém as transações mineradas.
     - `Timestamp:` Data e hora de criação do bloco.
     - `Data:` Lista de transações incluídas no bloco.
     - `Hash:` Hash do bloco.
     - `Hash Prev:` Hash do bloco anterior (bloco gênesis).

4. Histórico de Transações:
   - O histórico de transações para o endereço `AA1234567890abcdef1234567890abcdef1234567890abcdef` mostra a transação de compra do item "Asus ROG" por 12 unidades.

5. Saldos dos Endereços:
   - **AA1234567890abcdef1234567890abcdef1234567890abcdef:** Saldo de 87 unidades após a compra do item "Asus ROG".
   - **CC1234567890abcdef1234567890abcdef1234567890abcdef:** Saldo de 96.5 unidades após a compra da "escritura da casa".
   - **BBabcdef1234567890abcdef1234567890abcdef1234567890:** Saldo de 12 unidades após a venda do item "Asus ROG".
   - **a5efe3cf66e61843288ace120382688de911b85adbc904438f67fca3e4cdacba:** Saldo de 1.5 unidades como recompensa de mineração.
   - **DDabcdef1234567890abcdef1234567890abcdef1234567890:** Saldo de 3 unidades após a venda da "escritura da casa".
   - **EE1234567890abcdef1234567890abcdef1234567890abcdef:** Saldo de 1.5 unidades como recompensa de mineração.

## Fontes de Estudo

- [Monitorando a propagação de transações de nó para mempool em redes EVM com Python](https://docs.chainstack.com/docs/monitoring-transaction-propagation-from-node-to-mempool-in-evm-networks-with-python#:~:text=Roll%20your%20own%20propagation%20test,and%20keep%20things%20moving%20smoothly.)
- [How Cardano Propagates Blocks and Transactions](https://medium.com/@ed.wacc1995/how-cardano-propagates-blocks-and-transactions-ae2694cce29a)

