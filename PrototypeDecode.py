import csv
import getpass
from cryptography.fernet import Fernet

password = getpass.getpass(prompt="Введите пароль для расшифровки ключей:")

half_key = f'h4g8dh4js7dn3hd6{password}'
full_key = f'oh4aqAgeKK_{half_key}='.encode()

cipher = Fernet(full_key)

with open('encrypted_private_keys.csv', 'r') as input_file, open('decrypted_private_keys.txt', 'w') as output_file:
    reader = csv.reader(input_file)
    next(reader) # skip header
    for row in reader:
        encrypted_private_key = row[1].encode()
        private_key = cipher.decrypt(encrypted_private_key).decode()
        output_file.write(f'{private_key}\n')

