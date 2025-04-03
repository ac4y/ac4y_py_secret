from ac4y_py_secret import xor_encrypt_decrypt

key = "my_secret_key"
message = "Titkos üzenet"

encrypted_message = xor_encrypt_decrypt(message, key)
print(f"Titkosított üzenet: {encrypted_message}")

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print(f"Visszafejtett üzenet: {decrypted_message}")
