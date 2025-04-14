# Password Generator

A flexible Python-based password generator that creates secure passwords with various complexity options and includes a built-in password management system.

## Features

- **Multiple Password Types**:
  - Random: Mix of lowercase, uppercase, numbers, and special characters
  - Word-based: Words separated by a customizable character
  - Memorable: Word + numbers + special characters + uppercase letters
  - PIN: Digits only

- **Customizable Settings**:
  - Specify password length
  - Choose separator character for word-based passwords

- **Password Management**:
  - Save generated passwords with descriptions
  - Unique, timestamped filenames for easy reference
  - List and view saved passwords

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. No external dependencies required - just standard Python libraries!

## Usage

Run the program:

```
python password.py
```

### Menu Options

1. **Generate a new password**
   - Enter desired length
   - Select password type
   - View generated password
   - Optionally save with description

2. **List saved passwords**
   - View all previously saved passwords with timestamps and descriptions

3. **View a saved password**
   - Select a specific password file to view its contents

4. **Exit**
   - Close the application

### Sample Usage Flow

```
==== Password Generator ====

Options:
1. Generate a new password
2. List saved passwords
3. View a saved password
4. Exit

Enter your choice (1-4): 1

Enter desired password length: 12

Password Types:
1. Random (mix of letters, numbers, special characters)
2. Words (words separated by a character)
3. Memorable (word + numbers + special characters)
4. PIN (digits only)

Choose password type (1-4): 1

Generated Password: bJ4$kP8!aZ2x

Do you want to save this password? (y/n): y
Enter a purpose/description for this password: GitHub account
Password saved to file: passwords/pwd_20240414_152233_abcde.json
```

## Security Notes

- Passwords are stored in plaintext JSON files on your local system
- For increased security, consider encrypting the password files or implementing additional security measures
- This tool is intended for personal use and basic password management

## Future Enhancements

- Password strength meter
- Password encryption
- Import/export functionality
- GUI interface
- Custom word dictionary support

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Python's standard libraries
- Inspired by the need for quick, customizable password generation
