from node import Node
from network import Network, print_blockchain, consultar_historico_endereco
from ecdsa import SigningKey, SECP256k1
import json

my_node = Node("localhost")
network = Network(my_node)
network.join_network()

# Inicializando saldos para os endereços
network.blockchain_memory.balances['AA1234567890abcdef1234567890abcdef1234567890abcdef'] = 100
network.blockchain_memory.balances['CC1234567890abcdef1234567890abcdef1234567890abcdef'] = 100

# Gerando chaves para o comprador
comprador_sk = SigningKey.generate(curve=SECP256k1)
comprador_vk = comprador_sk.get_verifying_key()

# Gerando chaves para o vendedor
vendedor_sk = SigningKey.generate(curve=SECP256k1)
vendedor_vk = vendedor_sk.get_verifying_key()

compra1 = {
    'item': 'Asus ROG',  
    'valor': 12,  
    'taxa': 1,  # Adiciona a taxa de transação
    'comprador': 'AA1234567890abcdef1234567890abcdef1234567890abcdef',  # 50 caracteres
    'vendedor': 'BBabcdef1234567890abcdef1234567890abcdef1234567890'   # 50 caracteres
}

doc = {
    'item': 'escritura da casa',  
    'valor': 3, 
    'taxa': 0.5,  # Adiciona a taxa de transação
    'comprador': 'CC1234567890abcdef1234567890abcdef1234567890abcdef',  # 50 caracteres
    'vendedor': 'DDabcdef1234567890abcdef1234567890abcdef1234567890'   # 50 caracteres
}

# Assinando as transações
compra1_signature = comprador_sk.sign(json.dumps(compra1, sort_keys=True).encode()).hex()
doc_signature = comprador_sk.sign(json.dumps(doc, sort_keys=True).encode()).hex()

# Adicionando as transações à mempool
network.blockchain_memory.add_transaction(compra1, compra1_signature, comprador_vk.to_string().hex())
network.propagate_transaction(compra1)  # Propaga a transação para outros nós

network.blockchain_memory.add_transaction(doc, doc_signature, comprador_vk.to_string().hex())
network.propagate_transaction(doc)  # Propaga a transação para outros nós

# Mineração das transações pendentes
miner_address = 'EE1234567890abcdef1234567890abcdef1234567890abcdef'
network.blockchain_memory.mine_pending_transactions(miner_address)

# Imprimindo a blockchain após as transações
print_blockchain(network.blockchain_memory.chain)

# Consultando o histórico de transações de um endereço
endereco_comprador = 'AA1234567890abcdef1234567890abcdef1234567890abcdef'
consultar_historico_endereco(endereco_comprador, network.blockchain_memory)

# Imprimindo os saldos dos endereços
print("\nSaldos dos endereços:")
for endereco, saldo in network.blockchain_memory.balances.items():
    print(f"Endereço: {endereco}, Saldo: {saldo}")