import datetime as date  
from block import Block  
import re  # Importa o módulo para expressões regulares (regex)
import logging

# Gerenciador de toda a estrutura de blocos na blockchain
class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.transaction_history = {}  # Dicionário para armazenar o histórico de transações por endereço
        self.balances = {}  # Dicionário para armazenar os saldos dos endereços

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    def add_block(self, new_block):
        new_block.prev_hash = self.chain[-1].hash
        new_block.mine_block(self.difficulty)  # Chama o método de mineração
        self.chain.append(new_block)
        self.update_balances(new_block)  # Atualiza os saldos após adicionar o bloco

    def add_transaction(self, transaction_data):
        comprador = transaction_data.get('comprador', '')
        vendedor = transaction_data.get('vendedor', '')
        valor = transaction_data.get('valor', 0)
        taxa = transaction_data.get('taxa', 0)

        if not self.is_valid_address(comprador) or not self.is_valid_address(vendedor):
            logging.error(f"Transação rejeitada: endereços inválidos - Comprador: {comprador}, Vendedor: {vendedor}\n")
            return

        if valor <= 0 or taxa < 0:
            logging.error(f"Transação rejeitada: valor ou taxa inválidos - Valor: {valor}, Taxa: {taxa}\n")
            return

        if self.balances.get(comprador, 0) < valor + taxa:
            logging.error(f"Transação rejeitada: saldo insuficiente - Comprador: {comprador}, Saldo: {self.balances.get(comprador, 0)}, Valor: {valor}, Taxa: {taxa}\n")
            return

        # Adiciona a transação à blockchain
        index = len(self.chain)
        timestamp = date.datetime.now()
        new_block = Block(index, timestamp, transaction_data, self.chain[-1].hash, reward=taxa)
        self.add_block(new_block)

        # Registra a transação no histórico de cada endereço
        self._update_transaction_history(comprador, transaction_data)
        self._update_transaction_history(vendedor, transaction_data)

    def _update_transaction_history(self, address, transaction_data):
        if address not in self.transaction_history:
            self.transaction_history[address] = []  # Cria uma nova lista se o endereço não existir no histórico
        self.transaction_history[address].append(transaction_data)  # Adiciona a transação à lista de transações do endereço

    def get_transaction_history(self, address):
        # Retorna o histórico de transações de um endereço específico
        return self.transaction_history.get(address, [])

    def is_valid_address(self, address):
        address = address.strip().lower()
        print(f"\nVerificando endereço: {address}")

        if len(address) != 50:
            print(f"Endereço com comprimento incorreto: {len(address)}")
            return False

        pattern = r'^[a-zA-Z]{2}[0-9a-fA-F]{48}$'

        valid = bool(re.match(pattern, address))
        print(f"Endereço {'válido' if valid else 'inválido'}: {repr(address)}")
        return valid

    def update_balances(self, block):
        data = block.data
        comprador = data.get('comprador', '')
        vendedor = data.get('vendedor', '')
        valor = data.get('valor', 0)
        taxa = data.get('taxa', 0)

        if comprador:
            self.balances[comprador] = self.balances.get(comprador, 0) - valor - taxa
        if vendedor:
            self.balances[vendedor] = self.balances.get(vendedor, 0) + valor
        minerador = block.prev_hash  # Assumindo que o minerador é o nó anterior
        self.balances[minerador] = self.balances.get(minerador, 0) + taxa