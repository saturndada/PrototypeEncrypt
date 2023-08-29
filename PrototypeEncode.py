import csv
import getpass
from cryptography.fernet import Fernet
from web3 import Web3

w3 = Web3(Web3.HTTPProvider())

password = getpass.getpass(prompt="Введите пароль для зашифровки приватных ключей из 16 символов используя цифры и буквы разного регистра без использования спец символов:")

half_key = f'h4g8dh4js7dn3hd6{password}'
full_key = f'oh4aqAgeKK_{half_key}='.encode()

cipher = Fernet(full_key)

with open('private.txt', 'r') as input_file, open('encrypted_private_keys.csv', 'w', newline='') as output_file:
    reader = input_file.readlines()
    writer = csv.writer(output_file)

    writer.writerow(['Адрес', 'Зашифрованный приватный ключ'])

    for row in reader:
        private_key = row.strip()
        address = w3.to_checksum_address(w3.eth.account.from_key(private_key).address)
        encrypted_private_key = cipher.encrypt(private_key.encode())
        writer.writerow([address, encrypted_private_key.decode()])

print('приватные ключи зашифрованны вашим паролем и сохранены в файл encrypted_private_keys.csv, теперь вы можете удалить private.txt. Если потребуется снова получить приватные ключи в тхт формате, воспользуйтесь модулем PrototypeDecode.py')        
