from Crypto.Cipher import AES

def decrypt_file(input_file, key_file, bytes_to_encrypt=153605):
    # Đọc khóa từ file
    with open(key_file, 'rb') as f:
        key = f.read()
    
    # Đọc file mã hóa
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Tách IV, ciphertext và phần không mã hóa
    iv = encrypted_data[:AES.block_size]
    # Tính độ dài ciphertext sau khi đệm
    padded_length = ((bytes_to_encrypt // AES.block_size) + 1) * AES.block_size
    ciphertext = encrypted_data[AES.block_size:AES.block_size + padded_length]
    remaining_data = encrypted_data[AES.block_size + padded_length:]
    
    # Khởi tạo cipher và giải mã
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)
    
    # Loại bỏ đệm
    padding_length = padded_data[-1]
    plaintext = padded_data[:-padding_length]
    
    # Ghi đè lên file gốc
    with open(input_file, 'wb') as f:
        f.write(plaintext + remaining_data)
    
    print(f"Đã giải mã và ghi đè lên: {input_file}")

if __name__ == "__main__":
    input_file = 'input.mov'
    key_file = 'key.bin'
    decrypt_file(input_file, key_file)