import hashlib

class QGB_Genesis:
    def __init__(self):
        # DATOS REALES EXTRAÍDOS DE TU EJECUCIÓN EN IBM TORINO
        self.timestamp = "2026-01-08T10:56:58.228322Z"
        self.job_id = "d5foqunea9qs73904cgg"
        self.backend = "ibm_torino"
        self.shots = 2500
        self.supply = 21000000
        self.prev_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.memo = "QGB NETWORK: IN QUANTUM VERITAS. GENESIS CREATED BY SAUL MARTIN CLETO."

    def calculate_genesis_hash(self):
        # Concatenamos todos tus datos únicos
        block_string = f"{self.timestamp}{self.job_id}{self.backend}{self.shots}{self.supply}{self.prev_hash}{self.memo}"
        # Aplicamos SHA-256
        return hashlib.sha256(block_string.encode()).hexdigest()

# EJECUCIÓN
qgb = QGB_Genesis()
genesis_hash = qgb.calculate_genesis_hash()

print("--- REPORTE DE CREACIÓN DE RED QGB ---")
print(f"Timestamp: {qgb.timestamp}")
print(f"Quantum Proof ID: {qgb.job_id}")
print(f"Supply Total: {qgb.supply} QGB")
print("-" * 50)
print(f"HASH GÉNESIS OFICIAL (ID DE LA RED):")
print(f"{genesis_hash}")
print("-" * 50)
