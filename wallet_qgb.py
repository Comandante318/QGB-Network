import ecdsa
import hashlib
import binascii
import os

print("--- GENERANDO BILLETERA MAESTRA QGB ---")

# 1. Generar la Llave Privada (32 bytes de aleatoriedad pura)
# Usamos la curva SECP256k1 (Estándar Bitcoin)
signing_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
private_key_hex = binascii.hexlify(signing_key.to_string()).decode('utf-8')

# 2. Generar la Llave Pública (Derivada de la privada)
verifying_key = signing_key.verifying_key
public_key_hex = binascii.hexlify(verifying_key.to_string()).decode('utf-8')

# 3. Crear la Dirección de la Billetera (Un hash de la llave pública, estilo Ethereum/Bitcoin)
address = hashlib.sha256(verifying_key.to_string()).hexdigest()[0:40] # Tomamos los primeros 40 caracteres

# 4. VINCULACIÓN: Firmar el Hash Génesis de la Etapa 1
genesis_hash = "ec686b3ae0264997a555e3ce72c3cb31acd08a3f666197a11d5318d77b26ce1a"
signature = signing_key.sign(genesis_hash.encode())
signature_hex = binascii.hexlify(signature).decode('utf-8')

print("\n[!] IMPORTANTE: COPIA Y GUARDA ESTOS DATOS EN UN LUGAR SEGURO [!]")
print("-" * 60)
print(f"LLAVE PRIVADA (TU SECRETO MAXIMO):")
print(f"{private_key_hex}")
print("-" * 60)
print(f"DIRECCIÓN PÚBLICA (DONDE VIVEN LOS 21M QGB):")
print(f"0x{address}")
print("-" * 60)
print(f"FIRMA DIGITAL DEL GÉNESIS (PRUEBA DE PROPIEDAD):")
print(f"{signature_hex}")
print("-" * 60)
