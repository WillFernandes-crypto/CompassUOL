from node import Node
from network import Network, print_blockchain, consultar_historico_endereco

def test_propagation():
    # Teste de propagação de blocos e transações
    node1 = Node("localhost1")
    node2 = Node("localhost2")
    network1 = Network(node1)
    network2 = Network(node2)

    transaction = {
        'item': 'Produto A',
        'valor': 10,
        'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',
        'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890',
        'taxa': 1
    }
    node1.blockchain.add_transaction(transaction)
    node1.propagate_block(node1.blockchain.chain[-1])

    assert len(node2.blockchain.chain) == 1, "Node2 não recebeu o bloco."

def test_fork_resolution():
    # Teste de resolução de conflitos (forks)
    node1 = Node("localhost1")
    node2 = Node("localhost2")
    network1 = Network(node1)
    network2 = Network(node2)

    transaction1 = {
        'item': 'Produto A',
        'valor': 10,
        'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',
        'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890',
        'taxa': 1
    }
    transaction2 = {
        'item': 'Produto B',
        'valor': 20,
        'comprador': 'CC1234567890abcdef1234567890abcdef1234567890abcdef',
        'vendedor': 'DDabcdef1234567890abcdef1234567890abcdef1234567890',
        'taxa': 2
    }
    node1.blockchain.add_transaction(transaction1)
    node2.blockchain.add_transaction(transaction2)

    node1.propagate_block(node1.blockchain.chain[-1])
    node2.propagate_block(node2.blockchain.chain[-1])

    node1.blockchain.resolve_conflicts(node2.blockchain.chain)
    assert len(node1.blockchain.chain) == 2, "Node1 não adotou a cadeia mais longa."

def test_balance_control():
    # Teste de controle de saldos
    node = Node("localhost")
    network = Network(node)

    transaction = {
        'item': 'Produto A',
        'valor': 10,
        'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',
        'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890',
        'taxa': 1
    }
    node.blockchain.add_transaction(transaction)

    assert node.blockchain.get_balance('AA1234567890abcdef1234567890abcdef1234567890abcdef') == -10, "Saldo do comprador não está correto."
    assert node.blockchain.get_balance('BBabcdef1234567890abcdef1234567890abcdef1234567890') == 9, "Saldo do vendedor não está correto."

def test_transaction_fees_and_rewards():
    # Teste de taxas de transação e recompensas
    node = Node("localhost")
    network = Network(node)

    transaction1 = {
        'item': 'Produto A',
        'valor': 10,
        'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',
        'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890',
        'taxa': 1
    }
    transaction2 = {
        'item': 'Produto B',
        'valor': 20,
        'comprador': 'CC1234567890abcdef1234567890abcdef1234567890abcdef',
        'vendedor': 'DDabcdef1234567890abcdef1234567890abcdef1234567890',
        'taxa': 2
    }

    node.blockchain.add_transaction(transaction1)
    node.blockchain.add_transaction(transaction2)

    new_block = node.blockchain.chain[-1]
    total_fees = transaction1['taxa'] + transaction2['taxa']
    expected_reward = 5 + total_fees  # Supondo que a recompensa base seja 5

    assert new_block.data['recompensa'] == expected_reward, "Recompensa do minerador não está correta."

# Código principal
my_node = Node("localhost")
network = Network(my_node)
network.join_network()

compra1 = {
    'item': 'Asus ROG',  
    'valor': 12,  
    'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',  # 50 caracteres
    'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890'   # 50 caracteres
}

doc = {
    'item': 'escritura da casa',  
    'valor_pago_ao_cartorio': 3, 
    'comprador': 'CC1234567890abcdef1234567890abcdef1234567890abcdef12',  # 52 caracteres
    'vendedor': 'DDabcdef1234567890abcdef1234567890abcdef1234567890ab'   # 52 caracteres
}

# Adicionando as transações à blockchain
network.blockchain_memory.add_transaction(compra1)
network.blockchain_memory.add_transaction(doc)

# Imprimindo a blockchain após as transações
print_blockchain(network.blockchain_memory.chain)

# Consultando o histórico de transações de um endereço
endereco_comprador = 'AA1234567890abcdef1234567890abcdef1234567890abcdef'
consultar_historico_endereco(endereco_comprador, network.blockchain_memory)

# Executando os testes
test_propagation()
test_fork_resolution()
test_balance_control()
test_transaction_fees_and_rewards()
