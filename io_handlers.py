import csv
import os
import json
import datetime
import random
import string
from crypto import encrypt_data, decrypt_data

def import_passwords(filepath, encryption_key=None):
    """Import passwords from a CSV file"""
    imported_count = 0
    
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Extract data from CSV
                password = row.get('password', '')
                purpose = row.get('purpose', '')
                
                # Check if we should encrypt
                encrypt = encryption_key is not None
                
                if encrypt:
                    password = encrypt_data(password, encryption_key)
                
                # Generate filename
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
                filename = f"passwords/pwd_{timestamp}_{random_string}.json"
                
                # Create password data
                password_data = {
                    "password": password,
                    "purpose": purpose,
                    "encrypted": encrypt,
                    "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "imported": True
                }
                
                # Save to file
                with open(filename, 'w') as file:
                    json.dump(password_data, file, indent=4)
                
                imported_count += 1
                
        return imported_count
    except Exception as e:
        print(f"Error importing passwords: {e}")
        return 0

def export_passwords(filepath, decryption_key=None):
    """Export passwords to a CSV file"""
    export_count = 0
    
    if not os.path.exists("passwords"):
        print("No passwords to export.")
        return 0
    
    try:
        with open(filepath, 'w', newline='') as csvfile:
            fieldnames = ['purpose', 'password', 'created', 'encrypted']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for filename in os.listdir("passwords"):
                if filename.endswith('.json'):
                    file_path = os.path.join("passwords", filename)
                    
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        
                        password = data.get('password', '')
                        encrypted = data.get('encrypted', False)
                         
                        if encrypted and decryption_key:
                            try:
                                password = decrypt_data(password, decryption_key)
                                encrypted = False  
                            except: 
                                pass
                        
                        row = {
                            'purpose': data.get('purpose', ''),
                            'password': password,
                            'created': data.get('created', ''),
                            'encrypted': str(encrypted)
                        }
                        
                        writer.writerow(row)
                        export_count += 1
        
        return export_count
    except Exception as e:
        print(f"Error exporting passwords: {e}")
        return 0
