import random
import string
import os
import datetime
import json

def generate_random_password(length):
    
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_word_password(length, separator='.'):
    words = ['apple', 'banana', 'cherry', 'diamond', 'elephant', 'forest', 'garden',
             'house', 'island', 'jungle', 'kiwi', 'lemon', 'mountain', 'notebook',
             'orange', 'penguin', 'quiet', 'river', 'summer', 'tiger', 'umbrella',
             'violet', 'winter', 'xylophone', 'yellow', 'zebra', 'dog', 'cat',
             'tree', 'book', 'phone', 'computer', 'music', 'dance', 'light']
    
    password = []
    current_length = 0
    
    while current_length < length:
        word = random.choice(words)

        if current_length + len(word) + len(separator) > length:
            break
        password.append(word)
        current_length += len(word) + len(separator)
    
    
    result = separator.join(password)
    return result

def generate_memorable_password(length):
    words = ['apple', 'banana', 'cherry', 'diamond', 'elephant', 'forest', 'garden',
             'house', 'island', 'jungle', 'kiwi', 'lemon', 'mountain', 'notebook']
    
    word = random.choice(words)
    remaining_length = length - len(word)
    
    if remaining_length <= 0:
        return word[:length]
    

    digits_length = min(remaining_length, 4)
    digits = ''.join(random.choice(string.digits) for _ in range(digits_length))
    remaining_length -= digits_length
    

    special_chars = "!@#$%^&*"
    special_length = min(remaining_length, 2)
    special = ''.join(random.choice(special_chars) for _ in range(special_length))
    remaining_length -= special_length
    
 
    uppercase_length = min(remaining_length, 2)
    uppercase = ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase_length))
    
    
    password = word + digits + special + uppercase
    return password

def generate_pin_password(length):
    password = ''.join(random.choice(string.digits) for _ in range(length))
    return password

def save_password(password, purpose=""):
    if not os.path.exists("passwords"):
        os.makedirs("passwords")
    
 
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    filename = f"passwords/pwd_{timestamp}_{random_string}.json"
    
  
    password_data = {
        "password": password,
        "purpose": purpose,
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
                    print(f"{i}. {filename} - Purpose: {purpose} - Created: {created}")
            except:
                print(f"{i}. {filename} - [Error reading file]")

def view_password(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("\nPassword Details:")
            print(f"Password: {data['password']}")
            print(f"Purpose: {data.get('purpose', 'No purpose specified')}")
            print(f"Created: {data.get('created', 'Unknown date')}")
    except:
        print("Error reading the password file.")

def main():
    print("==== Password Generator ====")
    
    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. List saved passwords")
        print("3. View a saved password")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            try:
                length = int(input("\nEnter desired password length: "))
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            
     
            print("\nPassword Types:")
            print("1. Random (mix of letters, numbers, special characters)")
            print("2. Words (words separated by a character)")
            print("3. Memorable (word + numbers + special characters)")
            print("4. PIN (digits only)")
            
            type_choice = input("\nChoose password type (1-4): ")
            
      
            if type_choice == '1':
                password = generate_random_password(length)
            elif type_choice == '2':
                separator = input("Enter separator character (default '.'): ") or '.'
                password = generate_word_password(length, separator)
            elif type_choice == '3':
                password = generate_memorable_password(length)
            elif type_choice == '4':
                password = generate_pin_password(length)
            else:
                print("Invalid choice. Using random type.")
                password = generate_random_password(length)
             
            print(f"\nGenerated Password: {password}")
            
            save_choice = input("\nDo you want to save this password? (y/n): ").lower()
            if save_choice == 'y':
                purpose = input("Enter a purpose/description for this password: ")
                filename = save_password(password, purpose)
                print(f"Password saved to file: {filename}")
        
        elif choice == '2':
            list_saved_passwords()
        
        elif choice == '3':
            list_saved_passwords()
            password_dir = "passwords"
            if os.path.exists(password_dir) and os.listdir(password_dir):
                file_name = input("\nEnter the filename to view (e.g., pwd_20240414_123456_abcde.json): ")
                view_password(f"{password_dir}/{file_name}")
            else:
                print("No password files available to view.")
        
        elif choice == '4':
            print("Thank you for using the Password Generator.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
