import json
import os
import datetime

class QGB_Core:
    def __init__(self):
        self.db_file = "qgb_database.json"
        self.genesis_address = "0xd0aa7d261271b8ad9e5a9467c019b4b1addf83ce"
        self.marketing_address = "0xMARKETING_FUND_DEV_ALLOCATION_888"
        self.ledger = {}
        
        # VERIFICACIÓN DE EXISTENCIA
        if os.path.exists(self.db_file):
            print(" [i] Base de datos encontrada. Cargando historia...")
            self.load_data()
        else:
            print(" [!] Iniciando nueva red desde cero...")
            self.create_new_chain()

    def create_new_chain(self):
        # Estado inicial (Solo ocurre la primera vez)
        self.ledger = {
            self.genesis_address: 21000000.00,
            self.marketing_address: 0.00
        }
        self.save_data()

    def save_data(self):
        # Guardamos el estado actual en el disco duro
        with open(self.db_file, 'w') as f:
            json.dump(self.ledger, f, indent=4)
        print(" [SISTEMA] Ledger guardado en disco.")

    def load_data(self):
        # Leemos el estado desde el disco duro
        with open(self.db_file, 'r') as f:
            self.ledger = json.load(f)

    def transfer(self, sender, receiver, amount):
        print(f"\n[Solicitud] Transferir {amount} QGB...")
        
        if sender not in self.ledger:
            self.ledger[sender] = 0.00
            
        if self.ledger[sender] >= amount:
            self.ledger[sender] -= amount
            if receiver not in self.ledger:
                self.ledger[receiver] = 0.00
            self.ledger[receiver] += amount
            
            # ¡AQUÍ ESTÁ LA CLAVE! GUARDAMOS INMEDIATAMENTE
            self.save_data() 
            print(" [OK] Transacción confirmada y grabada en piedra.")
            return True
        else:
            print(" [X] Error: Fondos insuficientes.")
            return False

    def show_balance(self):
        print("\n" + "="*50)
        print("       ESTADO ACTUAL (PERSISTENTE)      ")
        print("="*50)
        print(f" ADMIN (Tú):      {self.ledger.get(self.genesis_address, 0):,.2f} QGB")
        print(f" MARKETING:       {self.ledger.get(self.marketing_address, 0):,.2f} QGB")
        print("="*50)

# --- PANEL DE CONTROL ---
system = QGB_Core()
system.show_balance()

# PREGUNTA INTERACTIVA
print("\n¿Deseas realizar una nueva transacción hoy?")
decision = input("Escribe 'si' para enviar 1000 QGB a Marketing, o 'no' para salir: ")

if decision.lower() == 'si':
    system.transfer(system.genesis_address, system.marketing_address, 1000.00)
    system.show_balance()
else:
    print("Saliendo... Tus datos están seguros.")
