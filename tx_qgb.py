import datetime

class QGB_Network:
    def __init__(self):
        self.ledger = {} 
        # TUS DATOS CONFIRMADOS
        self.genesis_address = "0xd0aa7d261271b8ad9e5a9467c019b4b1addf83ce"
        self.marketing_address = "0xMARKETING_FUND_DEV_ALLOCATION_888" # Una dirección destino simulada
        self.total_supply = 21000000.0000
        
        # Iniciar la red con los fondos en tu cuenta
        self.ledger[self.genesis_address] = self.total_supply
        self.ledger[self.marketing_address] = 0.00

    def transfer(self, sender, receiver, amount):
        print(f"\n[solicitud] Enviando {amount} QGB de {sender[:6]}... a {receiver[:10]}...")
        
        # 1. Verificación de fondos
        if self.ledger.get(sender, 0) < amount:
            print(" [X] ERROR: Fondos insuficientes.")
            return False
        
        # 2. Ejecución de la transacción (Atomicidad)
        self.ledger[sender] -= amount
        self.ledger[receiver] += amount
        
        # 3. Confirmación
        print(" [OK] Transacción Exitosa. Bloque actualizado.")
        return True

    def print_status(self):
        print("\n" + "="*50)
        print("       ESTADO DEL LIBRO CONTABLE (LEDGER)      ")
        print("="*50)
        print(f" TU BILLETERA (Admin):   {self.ledger[self.genesis_address]:,.4f} QGB")
        print(f" BILLETERA MARKETING:    {self.ledger[self.marketing_address]:,.4f} QGB")
        print("="*50)

# --- EJECUCIÓN DE LA PRUEBA EN VIVO ---

net = QGB_Network()

print("\n--- 1. ESTADO INICIAL ---")
net.print_status()

# Simulamos una pausa dramática
import time
time.sleep(1)

print("\n--- 2. EJECUTANDO PRIMERA TRANSACCIÓN ---")
# Estás enviando 5,000 monedas
net.transfer(net.genesis_address, net.marketing_address, 5000.00)

print("\n--- 3. ESTADO FINAL ---")
net.print_status()
