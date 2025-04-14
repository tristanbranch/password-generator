#!/usr/bin/env python3
import os
import sys
from generators import generate_random_password, generate_word_password, generate_memorable_password, generate_pin_password
from storage import save_password, list_saved_passwords, view_password
from utils import check_password_strength, load_custom_dictionary, save_custom_dictionary
from crypto import encrypt_data, decrypt_data, create_key_from_password
from io_handlers import import_passwords, export_passwords

def print_header():
    print("\n" + "="*50)
    print("           SECURE PASSWORD MANAGER")
    print("="*50)

def generate_password_menu():
    try:
        length = int(input("\nEnter desired password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return None, None
    except ValueError:
        print("Please enter a valid number.")
        return None, None
    
    print("\nPassword Types:")
    print("1. Random (mix of letters, numbers, special characters)")
    print("2. Words (words separated by a character)")
    print("3. Memorable (word + numbers + special characters)")
    print("4. PIN (digits only)")
    
    type_choice = input("\nChoose password type (1-4): ")
    
    custom_words = load_custom_dictionary()
    
    if type_choice == '1':
        password = generate_random_password(length)
    elif type_choice == '2':
        separator = input("Enter separator character (default '.'): ") or '.'
        password = generate_word_password(length, separator, custom_words)
    elif type_choice == '3':
        password = generate_memorable_password(length, custom_words)
    elif type_choice == '4':
        password = generate_pin_password(length)
    else:
        print("Invalid choice. Using random type.")
        password = generate_random_password(length)
    
    strength, details = check_password_strength(password)
    
    print(f"\nGenerated Password: {password}")
    print(f"Password Strength: {strength}")
    print(f"Details: {details}")
    
    return password, strength

def manage_dictionary_menu():
    print("\nCustom Dictionary Management:")
    print("1. View current dictionary")
    print("2. Add new words")
    print("3. Reset to default dictionary")
    print("4. Back to main menu")
    
    choice = input("\nEnter your choice (1-4): ")
    
    custom_words = load_custom_dictionary()
    
    if choice == '1':
        if not custom_words:
            print("No custom dictionary found. Using default.")
        else:
            print("\nCurrent Dictionary:")
            for word in custom_words:
                print(f"- {word}")
    elif choice == '2':
        print("\nEnter words to add (one per line, blank line to finish):")
        while True:
            word = input().strip()
            if not word:
                break
            custom_words.append(word)
        save_custom_dictionary(custom_words)
        print(f"Dictionary updated with {len(custom_words)} words.")
    elif choice == '3':
        save_custom_dictionary([])
        print("Dictionary reset to default.")
    elif choice == '4':
        return
    else:
        print("Invalid choice.")

def main():
    if not os.path.exists("passwords"):
        os.makedirs("passwords")
    if not os.path.exists("data"):
        os.makedirs("data")
        
    print_header()
    
    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. List saved passwords")
        print("3. View a saved password")
        print("4. Check password strength")
        print("5. Import passwords from CSV")
        print("6. Export passwords to CSV")
        print("7. Manage custom word dictionary")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            password, strength = generate_password_menu()
            if password:
                save_choice = input("\nDo you want to save this password? (y/n): ").lower()
                if save_choice == 'y':
                    encrypt = input("Encrypt this password? (y/n): ").lower() == 'y'
                    if encrypt:
                        master_password = input("Enter master password for encryption: ")
                        key = create_key_from_password(master_password)
                        password = encrypt_data(password, key)
                    
                    purpose = input("Enter a purpose/description for this password: ")
                    filename = save_password(password, purpose, strength, encrypt)
                    print(f"Password saved to file: {filename}")
        
        elif choice == '2':
            list_saved_passwords()
        
        elif choice == '3':
            list_saved_passwords()
            password_dir = "passwords"
            if os.path.exists(password_dir) and os.listdir(password_dir):
                file_name = input("\nEnter the filename to view: ")
                full_path = f"{password_dir}/{file_name}"
                
                if os.path.exists(full_path):
                    encrypted = input("Is this password encrypted? (y/n): ").lower() == 'y'
                    if encrypted:
                        master_password = input("Enter master password for decryption: ")
                        key = create_key_from_password(master_password)
                        view_password(full_path, key)
                    else:
                        view_password(full_path)
                else:
                    print("File not found.")
            else:
                print("No password files available to view.")
        
        elif choice == '4':
            password = input("\nEnter password to check: ")
            strength, details = check_password_strength(password)
            print(f"Password Strength: {strength}")
            print(f"Details: {details}")
        
        elif choice == '5':
            filepath = input("\nEnter path to CSV file: ")
            if os.path.exists(filepath):
                master_password = input("Enter master password for encrypted passwords (leave blank if none): ")
                key = create_key_from_password(master_password) if master_password else None
                count = import_passwords(filepath, key)
                print(f"Successfully imported {count} passwords.")
            else:
                print("File not found.")
        
        elif choice == '6':
            filepath = input("\nEnter destination path for CSV export: ")
            master_password = input("Enter master password for encrypted passwords (leave blank if none): ")
            key = create_key_from_password(master_password) if master_password else None
            count = export_passwords(filepath, key)
            print(f"Successfully exported {count} passwords.")
        
        elif choice == '7':
            manage_dictionary_menu()
        
        elif choice == '8':
            print("Thank you for using the Password Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
