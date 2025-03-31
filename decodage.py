import string
from pathlib import Path

#Répertoire des différents fichier utilisés dans ce scrypt
old_message_path = Path("old_message.txt")
key_old_message_path = Path("key_old_message.txt")

new_message = Path("KENNEDY Théo.txt")

#Lecture des fichiers
with old_message_path.open('r') as file:
    old_message = file.read()

with key_old_message_path.open('r') as file:
    key_old_message = eval(file.read())

#Trier les clés
def extract_and_sort_keys(old_message: str, key_old_message: set) -> list:
    words = set(old_message.split())
    keys = sorted(words - key_old_message)
    return keys

def map_keys_to_alphabet(keys: list) -> dict:
    alphabet = string.ascii_uppercase + "0123456789"
    key_mapping = {key: alphabet[i] for i, key in enumerate(keys) if i < len(alphabet)}
    return key_mapping

keys = extract_and_sort_keys(old_message, key_old_message)

key_mapping = map_keys_to_alphabet(keys)

# Affichage des clés et de leur correspondance
print("Mapping des clés :")
for key, value in key_mapping.items():
    print(f"{key}: {value}")

def decode_message(old_message: str, key_mapping: dict) -> str:
    words = old_message.split()
    decoded_message = ''.join(key_mapping.get(word, '') for word in words)
    return decoded_message

#Affichage des messages décodés
decoded_message = decode_message(old_message, key_mapping)
print("Message décodé :")
print(decoded_message)

new_decoded_message = decode_message(new_message.read_text(), key_mapping)
print("Message décodé du nouveau fichier :")
print(new_decoded_message)

#Fonction pour encoder un message
def encode_message(message: str, key_mapping: dict) -> str:
    reverse_mapping = {v: k for k, v in key_mapping.items()}
    encoded_message = ' '.join(reverse_mapping.get(char, '') for char in message)
    return encoded_message

#Affichage du message encodé
message_to_encode = "CECI EST UN MESSAGE A ENCODER"
encoded_message = encode_message(message_to_encode, key_mapping)
print("Message encodé :")
print(encoded_message)
