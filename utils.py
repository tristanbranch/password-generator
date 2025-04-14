import re
import os
import json

def check_password_strength(password):
    if not password:
        return "Weak", "Empty password"
    
    score = 0
    details = []
    
    # Length check
    if len(password) < 8:
        details.append("Too short")
    elif len(password) >= 12:
        score += 2
        details.append("Good length")
    else:
        score += 1
        details.append("Acceptable length")
    
    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        details.append("No lowercase letters")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        details.append("No uppercase letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        details.append("No numbers")
    
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        details.append("No special characters")
    
    # Repetition and sequence checks
    if re.search(r'(.)\1\1', password):
        score -= 1
        details.append("Character repetition")
    
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)', password.lower()):
        score -= 1
        details.append("Sequential characters")
    
    # Common patterns check
    common_patterns = ['password', '123456', 'qwerty', 'admin', 'welcome', 'letmein']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        details.append("Common pattern detected")
    
    # Calculate strength rating
    if score <= 0:
        strength = "Very Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    # Format details
    if not details:
        details_text = "Excellent password!"
    else:
        details_text = ", ".join(details)
    
    return strength, details_text

def load_custom_dictionary():
    dict_path = "data/custom_dictionary.json"
    if not os.path.exists(dict_path):
        return []
    
    try:
        with open(dict_path, 'r') as file:
            return json.load(file)
    except:
        return []

def save_custom_dictionary(words):
    if not os.path.exists("data"):
        os.makedirs("data")
    
    dict_path = "data/custom_dictionary.json"
    with open(dict_path, 'w') as file:
        json.dump(words, file, indent=4)
