import json
import datetime

class QGB_Node:
    def __init__(self):
        self.chain = []
        self.ledger = {} # Aquí se guardan los saldos
        
        # DATOS DE LA RED (Tus datos confirmados)
        self.genesis_hash = "ec686b3ae0264997a555e3ce72c3cb31acd08a3f666197a11d5318d77b26ce1a"
        self.genesis_address = "0xd0aa7d261271b8ad9e5a9467c019b4b1addf83ce"
        self.total_supply = 21000000.0000
        
        # Iniciar la red
        self.create_genesis_block()

    def create_genesis_block(self):
        # El bloque 0 no tiene transacciones previas, es una emisión directa (Coinbase)
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.datetime.now()),
            'proof_hash': self.genesis_hash,
            'transactions': [
                {
                    'from': 'NETWORK_MINT',
                    'to': self.genesis_address,
                    'amount': self.total_supply,
                    'type': 'GENESIS_ALLOCATION'
                }
            ],
            'previous_hash': "0" * 64
        }
        self.chain.append(genesis_block)
        self.update_ledger(genesis_block['transactions'])

    def update_ledger(self, transactions):
        for tx in transactions:
            receiver = tx['to']
            amount = tx['amount']
            
            # Si la cuenta no existe en el libro, la creamos
            if receiver not in self.ledger:
                self.ledger[receiver] = 0.00
            
            self.ledger[receiver] += amount

    def get_balance(self, address):
        return self.ledger.get(address, 0.00)

    def print_chain_status(self):
        print("\n" + "="*60)
        print("          QGB NETWORK - NODO MAESTRO (LOCAL)          ")
        print("="*60)
        print(f" Estado de la Red: ONLINE")
        print(f" Bloques minados: {len(self.chain)}")
        print(f" Hash Génesis: {self.genesis_hash[:10]}...{self.genesis_hash[-10:]}")
        print("-" * 60)
        print(" [!] CONSULTA DE SALDO EN TIEMPO REAL")
        print(f" Dirección: {self.genesis_address}")
        
        balance = self.get_balance(self.genesis_address)
        print(f" SALDO ACTUAL: {balance:,.4f} QGB")
        print("="*60)

# EJECUCIÓN DEL NODO
node = QGB_Node()
node.print_chain_status()
