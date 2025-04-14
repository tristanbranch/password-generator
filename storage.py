import os
import json
import random
import string
import datetime
from crypto import decrypt_data

def save_password(password, purpose="", strength="", encrypted=False):
    if not os.path.exists("passwords"):
        os.makedirs("passwords")
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    filename = f"passwords/pwd_{timestamp}_{random_string}.json"
    
    password_data = {
        "password": password,
        "purpose": purpose,
        "strength": strength,
        "encrypted": encrypted,
        "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(filename, 'w') as file:
        json.dump(password_data, file, indent=4)
    
    return filename

def list_saved_passwords():
    if not os.path.exists("passwords"):
        print("No saved passwords found.")
        return
    
    files = os.listdir("passwords")
    if not files:
        print("No saved passwords found.")
        return
    
    print("\nSaved Passwords:")
    for i, filename in enumerate(files, 1):
        if filename.endswith('.json'):
            try:
                with open(f"passwords/{filename}", 'r') as file:
                    data = json.load(file)
                    purpose = data.get("purpose", "No purpose specified")
                    created = data.get("created", "Unknown date")
                    encrypted = "🔒 " if data.get("encrypted", False) else ""
                    strength = data.get("strength", "")
                    strength_indicator = f"[{strength}] " if strength else ""
                    print(f"{i}. {encrypted}{strength_indicator}{filename} - Purpose: {purpose} - Created: {created}")
            except:
                print(f"{i}. {filename} - [Error reading file]")

def view_password(filename, decryption_key=None):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            
            password = data['password']
            if data.get("encrypted", False) and decryption_key:
                try:
                    password = decrypt_data(password, decryption_key)
                except:
                    print("Error: Decryption failed. Incorrect password.")
                    return
            
            print("\nPassword Details:")
            print(f"Password: {password}")
            print(f"Purpose: {data.get('purpose', 'No purpose specified')}")
            print(f"Strength: {data.get('strength', 'Not evaluated')}")
            print(f"Created: {data.get('created', 'Unknown date')}")
            print(f"Encrypted: {'Yes' if data.get('encrypted', False) else 'No'}")
    except:
        print("Error reading the password file.")
