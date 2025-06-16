from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    # Đệm dữ liệu để có độ dài là bội số của 16
    padding_length = AES.block_size - len(data) % AES.block_size
    padding = bytes([padding_length]) * padding_length
    return data + padding

def encrypt_file(input_file, key_file, bytes_to_encrypt=153605):
    # Tạo khóa ngẫu nhiên
    key = get_random_bytes(32)  # Khóa 256-bit
    
    # Lưu khóa vào file
    with open(key_file, 'wb') as f:
        f.write(key)
    
    # Khởi tạo cipher với chế độ CBC
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Đọc file đầu vào
    with open(input_file, 'rb') as f:
        # Đọc phần cần mã hóa
        plaintext = f.read(bytes_to_encrypt)
        # Đọc phần còn lại (không mã hóa)
        remaining_data = f.read()
    
    # Thêm đệm và mã hóa phần đầu
    padded_data = pad(plaintext)
    ciphertext = cipher.encrypt(padded_data)
    
    # Ghi đè lên file gốc
    with open(input_file, 'wb') as f:
        f.write(iv + ciphertext + remaining_data)
    
    print(f"Đã mã hóa {bytes_to_encrypt} byte đầu tiên và ghi đè lên: {input_file}")
    print(f"Khóa đã được lưu vào: {key_file}")

if __name__ == "__main__":
    input_file = 'input.mov'
    key_file = 'key.bin'
    encrypt_file(input_file, key_file)