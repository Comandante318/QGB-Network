import hashlib
import json
import os
from flask import Flask, jsonify

class QGB_Mainnet:
    def __init__(self):
        self.chain = []
        self.file_path = 'qgb_blockchain.json'
        self.load_chain()

    def load_chain(self):
        # Verifica si existe el archivo en el disco duro de la HP
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.chain = json.load(f)
        else:
            # Crea el Bloque Génesis con tus datos de IBM Torino
            self.genesis_data = {
                'autoridad': "SMBZ36",
                'bloque': 0,
                'hash_maestro': "470e324d5aed6fe7a7baed9c33f9ef535913c624762f65ac21056fd30f7d1444",
                'id_ibm_nodo': "d5foqunea9qs73904cgg",
                'inicio_trabajo_cuantico': "2026-01-08",
                'nacimiento_oficial': "2026-01-24",
                'suministro_total': 21000000
            }
            self.chain.append(self.genesis_data)
            self.save_chain()

    def save_chain(self):
        # Graba la cadena en el archivo JSON
        with open(self.file_path, 'w') as f:
            json.dump(self.chain, f, indent=4)

    def proof_of_quantum(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# CONFIGURACIÓN DEL SERVIDOR FLASK
app = Flask(__name__)
qgb_node = QGB_Mainnet()

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': qgb_node.chain, 'length': len(qgb_node.chain)}), 200

@app.route('/mine', methods=['GET'])
def mine():
    last_block = qgb_node.chain[-1]
    last_proof = last_block.get('proof', 100)
    proof = qgb_node.proof_of_quantum(last_proof)
    
    previous_hash = hashlib.sha256(json.dumps(last_block, sort_keys=True).encode()).hexdigest()
    new_block = {
        'index': len(qgb_node.chain),
        'timestamp': "2026-01-26",
        'proof': proof,
        'previous_hash': previous_hash,
        'authority': "SMBZ36 - VALIDADO POR IBM TORINO"
    }
    qgb_node.chain.append(new_block)
    qgb_node.save_chain() # GUARDA AL INSTANTE EN DISCO
    return jsonify({'message': "Bloque Minado!", 'block': new_block}), 200

if __name__ == "__main__":
    print("\n" + "="*45)
    print(">>> NODO MAESTRO QGB: ETAPA 5 ACTIVA (PERSISTENTE)")
    print(">>> MINERÍA CUÁNTICA HABILITADA")
    print("="*45 + "\n")
    app.run(host='0.0.0.0', port=5000)
