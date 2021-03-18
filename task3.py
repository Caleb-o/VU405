"""
    Title:      'Task 3' - Convert and shift text with key - user program
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
    Updated:    18/3/2021
"""

import cipher, sys, os, time, testing


# Constants
TITLE: str = 'Caesar Cipher'
REST_TIME: float = 1.5
DEFAULT_KEY: int = 3


def clear() -> None:
    # Check if Windows or nix
    os.system('cls' if os.name == 'nt' else 'clear')


# Generic wait for user call
def enter_continue() -> None:
    time.sleep(REST_TIME / 2)
    input('Press Enter to continue...')


def encrypt(message: str, key: str) -> None:
    # Check inputs
    to_encrypt: str = message if len(message) > 0 else 'Hello.World!23'

    # Validate text for conversion to int
    try:
        shift_key: int = int(key) if len(key) > 0 else DEFAULT_KEY
    except (TypeError, ValueError):
        shift_key: int = DEFAULT_KEY

    # Invert key if below 0
    if shift_key < 0:
        shift_key *= -1
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(to_encrypt)
    
    print(f'Original text: \'{to_encrypt}\'')
    print(f'Encrypted [{shift_key}] text: \'{cipher.shift_text(ciphered_text, shift_key)}\'')


def decrypt(message: str, key: str) -> None:
    # Check inputs
    to_decrypt: str = message if len(message) > 0 else 'Hello.World!23'

    # Validate text for conversion to int
    try:
        shift_key: int = int(key) if len(key) > 0 else -DEFAULT_KEY
    except (TypeError, ValueError):
        shift_key: int = -DEFAULT_KEY

    # Invert key if above 0
    if shift_key > 0:
        shift_key *= -1
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(to_decrypt)
    
    print(f'Original text: \'{to_decrypt}\'')
    print(f'Decrypted [{shift_key}] text: \'{cipher.shift_text(ciphered_text, shift_key)}\'')


# Menu option functions
def opt_encrypt() -> None:
    """
        User operated encrypt.
    """
    to_encrypt: str = input('Enter text: ')
    shift_key: str = input(f'Enter a shift key (Default {DEFAULT_KEY}): ')
    
    encrypt(to_encrypt, shift_key)
    enter_continue()


def opt_decrypt() -> None:
    """
        User operated decrypt.
    """
    to_decrypt: str = input('Enter text: ')
    shift_key: str = input(f'Enter a negative shift key (Default {-DEFAULT_KEY}): ')
    
    decrypt(to_decrypt, shift_key)
    enter_continue()


def opt_help() -> None:
    """
        Program help menu.
    """
    print(f"""
Encrypt - Asks for a message and key to encrypt and shows the encrypted text.
Decrypt - Asks for an encrypted message and key to decrypt and shows the decrypted text.
Tests - Shows test cases, whether conversion and full encryption passes the test.
Quit - Exits the program.""")
    enter_continue()


def opt_tests() -> None:
    """
        Runs all the test cases to date.
    """
    testing.run_test_cases(testing.TestType.CONVERTED, 'Converted')
    testing.run_test_cases(testing.TestType.SHIFTED, 'Shifted')
    enter_continue()


def opt_quit() -> None:
    """
        Exits the program.
    """
    clear()
    sys.exit()


# All menu options dictionary with bound functions
menu_options: dict = {
    0 : ('Encrypt', opt_encrypt),
    1 : ('Decrypt', opt_decrypt),
    2 : ('Help', opt_help),
    3 : ('Tests', opt_tests),
    4 : ('Quit', opt_quit),
}

# Options for the command-line
cli_options: dict = {
    '-e':    encrypt,
    '-d':    decrypt,
}

def print_options(options: dict) -> None:
    """
        Prints out all menu options (or options provided - default is menu_options).
    """
    print(TITLE)

    # Print all options with numbers
    for op, i in zip(options, range(len(options))):
        print(f'{i + 1}. {options[i][0]}')


# Entry to program
def main(options: dict = menu_options) -> None:

    while(True):
        # Clear console and print menu options
        clear()
        print_options(options)

        inp = input('\nEnter # ')

        # Validate input
        if len(inp) > 0:
            try:
                inp = int(inp)
            except (TypeError, ValueError):
                print('Option must be a number!')
                time.sleep(REST_TIME)
                continue
        else:
            print('Please enter an option.')
            time.sleep(REST_TIME)
            continue

        # Run function from dictionary
        if len(options) > (inp-1) >= 0:
            clear()
            print(options[inp - 1][0])
            options[inp - 1][1]()
        else:
            print(f'Option must be between 1 and {len(options)}.')


# Entry point
if __name__ == '__main__':
    # Command line usage
    if len(sys.argv) > 1:
        # Check if arguments are correct length 
        if len(sys.argv) < 4:
            print('Command syntax: task3.py [type] [message] [key]\neg. task3.py -e "hello" 3')
        else:
            cmd = cli_options[sys.argv[1]](sys.argv[2], sys.argv[3])
    else:
        main()