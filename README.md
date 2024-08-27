# Password Manager

This project is a simple password manager that allows users to securely store and retrieve passwords using encryption. The passwords are stored in a text file and are encrypted using the `cryptography` library's `Fernet` symmetric encryption.

## Features

- **View stored passwords**: Decrypt and display all stored passwords.
- **Add new passwords**: Encrypt and save new passwords to the storage file.
- **Secure encryption**: Utilizes `Fernet` encryption to securely store passwords.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/aayush3692/password-manager.git
    cd password-manager
    ```

2. **Install the required packages**:

    Install the `cryptography` library if you haven't already:

    ```bash
    pip install cryptography
    ```

3. **Generate an encryption key** (if you don't have one):

    Before running the program for the first time, you need to generate an encryption key and save it to a file named `key.key`:

    ```python
    from cryptography.fernet import Fernet

    def write_key():
        """Generate and write a new encryption key to a file."""
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    ```

    Run this script to generate and save your encryption key.

4. **Create the passwords file**:

    Ensure you have a file named `passwords.txt` in the same directory as your script. This file will be used to store your encrypted passwords.

## Usage

1. **Run the program**:

    Execute the script using Python:

    ```bash
    python password_manager.py
    ```

2. **Follow the on-screen instructions**:

    - **View stored passwords**: Choose option `1` to decrypt and view all stored passwords.
    - **Add a new password**: Choose option `2` to add a new password (which will be encrypted and stored).
    - **Quit**: Choose option `3` to exit the program.

## Code Overview

- **`load_key()`**: Loads the encryption key from the `key.key` file.
- **`view(fer)`**: Decrypts and displays all passwords stored in `passwords.txt`.
- **`add(fer)`**: Encrypts and adds a new password to `passwords.txt`.
- **`main()`**: The main function that handles user input and calls other functions.

## Security

- **Encryption**: All passwords are encrypted using the `Fernet` symmetric encryption scheme before being stored.
- **Key Management**: Make sure to keep the `key.key` file secure, as it is required to decrypt your stored passwords.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [cryptography](https://cryptography.io/en/latest/) library.
