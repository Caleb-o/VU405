"""
    Title:      'Task 3' - Convert and shift text with key
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
    Updated:    4/3/2021
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


# Menu option functions
def encrypt() -> None:
    to_encrypt: str = input('Enter text: ')
    shift_key: str = input(f'Enter a shift key (Default {DEFAULT_KEY}): ')
    
    # Check inputs
    to_encrypt: str = to_encrypt if len(to_encrypt) > 0 else 'Hello.World!23'

    # Validate text for conversion to int
    try:
        shift_key: int = int(shift_key) if len(shift_key) > 0 else DEFAULT_KEY
    except (TypeError, ValueError):
        shift_key: int = DEFAULT_KEY
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(to_encrypt)
    
    print(f'Original text: \'{to_encrypt}\'')
    print(f'Encrypted [{shift_key}] text: \'{cipher.shift_text(ciphered_text, shift_key)}\'')

    enter_continue()


def decrypt() -> None:
    to_decrypt: str = input('Enter text: ')
    shift_key: str = input(f'Enter a negative shift key (Default {-DEFAULT_KEY}): ')
    
    # Check inputs
    to_decrypt: str = to_decrypt if len(to_decrypt) > 0 else 'Hello.World!23'

    # Validate text for conversion to int
    try:
        shift_key: int = int(shift_key) if len(shift_key) > 0 else -DEFAULT_KEY
    except (TypeError, ValueError):
        shift_key: int = -DEFAULT_KEY
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(to_decrypt)
    
    print(f'Original text: \'{to_decrypt}\'')
    print(f'Decrypted [{shift_key}] text: \'{cipher.shift_text(ciphered_text, shift_key)}\'')

    enter_continue()


def help() -> None:
    enter_continue()


def tests() -> None:
    """
        Runs all the test cases to date.
    """
    testing.run_test_cases(testing.TestType.CONVERTED, 'Converted')
    testing.run_test_cases(testing.TestType.SHIFTED, 'Shifted')
    enter_continue()


def quit() -> None:
    clear()
    sys.exit()


# CLI options
class cli_type:
    ENCRYPT: 0
    DECRYPT: 1
    HELP: 2

# Command line globals
CLI_KEY: int = DEFAULT_KEY
CLI_STR: str
CLI_TYPE: cli_type

# Command line option functions
def cli_set_key(key: int):
    pass


# All menu options dictionary with bound functions
menu_options: dict = {
    0 : ('Encrypt', encrypt),
    1 : ('Decrypt', decrypt),
    2 : ('Help', help),
    3 : ('Tests', tests),
    4 : ('Quit', quit),
}

cli_options: dict {
    'd':  
}

def print_options(options: dict) -> None:
    """
        Prints out all menu options (or options provided - default is menu_options).
    """
    print(TITLE)

    # Print all options with numbers
    for op, i in zip(options, range(len(options))):
        print(f'{i + 1}. {options[i][0]}')


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
        pass
    else:
        main()