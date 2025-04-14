# Terminal Password Manager

A secure, feature-rich password manager that runs entirely in the terminal.

## Features

- **Multiple Password Types**:
  - Random: Mix of lowercase, uppercase, numbers, and special characters
  - Word-based: Words separated by a customizable character
  - Memorable: Word + numbers + special characters + uppercase letters
  - PIN: Digits only

- **Password Strength Meter**:
  - Analyzes password security
  - Provides detailed feedback
  - Rates from "Very Weak" to "Very Strong"

- **Password Encryption**:
  - Optional encryption using Fernet symmetric encryption
  - Master password protection
  - Secure key derivation using PBKDF2

- **Custom Word Dictionary**:
  - Add your own words for word-based passwords
  - View and manage custom dictionary
  - Reset to default when needed

- **Import/Export Functionality**:
  - CSV import and export
  - Maintain encrypted status during transfer
  - Batch password management

- **Password Management**:
  - Save generated passwords with descriptions
  - Unique, timestamped filenames
  - List and view saved passwords

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the program:

```
python password.py
```

## Project Structure

- `password.py` - Main application script
- `generators.py` - Password generation functions
- `storage.py` - Password storage and retrieval
- `utils.py` - Utility functions including password strength checker
- `crypto.py` - Encryption and decryption functions
- `io_handlers.py` - Import/export functionality

## Security Notes

- Passwords can be stored encrypted using Fernet symmetric encryption
- Master password is never stored, only used to derive encryption keys
- Password strength meter helps create more secure passwords
