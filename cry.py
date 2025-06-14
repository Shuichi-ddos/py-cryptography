from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

# Chức năng mã hóa
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    
    # Chuyển đổi dữ liệu được mã hóa sang định dạng base64
    nonce = base64.b64encode(cipher.nonce).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    tag = base64.b64encode(tag).decode('utf-8')

    return nonce, ciphertext, tag


# Chức năng lưu tập tin
def save_encrypted_data(nonce, ciphertext, tag):
    # Lấy đường dẫn đến màn hình của người dùng
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Cryptography.txt")
    
    # Lưu dữ liệu đã mã hóa vào tệp
    with open(desktop_path, 'w') as file:
        file.write(f"Nonce: {nonce}\n")
        file.write(f"Ciphertext: {ciphertext}\n")
        file.write(f"Tag: {tag}\n")
    print(f"Tệp được mã hóa được lưu vào Desktop: {desktop_path}")


#Chức năng chính
def main():
    # Lấy văn bản đầu vào từ người dùng
    text = input("Nhập một số văn bản: ")

    # Tạo khóa mã hóa ngẫu nhiên có độ dài 16 byte
    key = get_random_bytes(16)

    # Quá trình mã hóa
    nonce, ciphertext, tag = encrypt_data(text, key)

    # Lưu dữ liệu đã mã hóa vào tệp
    save_encrypted_data(nonce, ciphertext, tag)

if __name__ == "__main__":
    main()