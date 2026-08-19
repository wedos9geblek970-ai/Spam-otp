#!/usr/bin/env python3
# ============================================================
# PROTECTED SCRIPT (AES-256-GCM ENCRYPTED)
# Tidak bisa dibaca tanpa password yang benar
# ============================================================

import sys
import base64
import zlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ============================================================
# DATA TERENKRIPSI (BASE64)
# ============================================================
ENCRYPTED_DATA = """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"""

# ============================================================
# FUNGSI DEKRIPSI
# ============================================================

def decrypt_and_run(encrypted_b64: str, password: str):
    """Dekripsi dan jalankan script"""
    data = base64.b64decode(encrypted_b64)
    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode('utf-8'))
    
    aesgcm = AESGCM(key)
    decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    
    # Decompress
    decompressed = zlib.decompress(decrypted)
    
    # Jalankan script
    exec(decompressed, {'__name__': '__main__'})

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("🔐 Protected Script - AES-256-GCM Encrypted")
        print("Usage: python this_script.py")
        sys.exit(0)
    
    try:
        import getpass as gp
        pwd = gp.getpass("🔑 Password: ")
        decrypt_and_run(ENCRYPTED_DATA, pwd)
    except Exception as e:
        print(f"❌ Error: Password salah atau file corrupt!\n   {e}")
        sys.exit(1)
