import random
import string

def generate_random_password(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_word_password(length, separator='.', custom_words=None):
    if custom_words and len(custom_words) > 0:
        words = custom_words
    else:
        words = ['apple', 'banana', 'cherry', 'diamond', 'elephant', 'forest', 'garden',
                'house', 'island', 'jungle', 'kiwi', 'lemon', 'mountain', 'notebook',
                'orange', 'penguin', 'quiet', 'river', 'summer', 'tiger', 'umbrella',
                'violet', 'winter', 'xylophone', 'yellow', 'zebra', 'dog', 'cat',
                'tree', 'book', 'phone', 'computer', 'music', 'dance', 'light']
    
    password = []
    current_length = 0
    
    while current_length < length:
        word = random.choice(words)
        if current_length + len(word) + len(separator) > length and password:
            break
        password.append(word)
        current_length += len(word) + len(separator)
    
    result = separator.join(password)
    return result[:length]

def generate_memorable_password(length, custom_words=None):
    if custom_words and len(custom_words) > 0:
        words = custom_words
    else:
        words = ['apple', 'banana', 'cherry', 'diamond', 'elephant', 'forest', 'garden',
                'house', 'island', 'jungle', 'kiwi', 'lemon', 'mountain', 'notebook']
    
    word = random.choice(words)
    if len(word) > length:
        return word[:length]
    
    remaining_length = length - len(word)
    
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
