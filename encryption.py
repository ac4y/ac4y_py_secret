# encryption.py

def xor_encrypt_decrypt(input_string, key):
    """Egyszerű XOR titkosítás és visszafejtés."""
    input_bytes = input_string.encode()
    key_bytes = key.encode()

    # Titkosítás (XOR művelet minden byte-on)
    output_bytes = bytearray()
    for i in range(len(input_bytes)):
        output_bytes.append(input_bytes[i] ^ key_bytes[i % len(key_bytes)])

    return bytes(output_bytes).decode(errors="ignore")
