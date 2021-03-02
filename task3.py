"""
    Title:      'Task 3' - Convert and shift text with key
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
    Updated:    2/3/2021
"""

from typing import Type
import cipher, sys, os, time


# Constants
REST_TIME: float = 1.5


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_continue() -> None:
    time.sleep(REST_TIME / 2)
    input('Press enter to continue...')


# Menu options
def encrypt() -> None:
    to_cipher: str = input('\nEnter text: ')
    shift_key: str = input('Enter a shift key: ')
    
    # Check inputs
    to_cipher = to_cipher if len(to_cipher) > 0 else 'Hello.World!23'
    shift_key = int(shift_key) if len(shift_key) > 0 else 3
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(to_cipher)
    
    print(f'Original text: \'{to_cipher}\'')
    print(f'Converted text: \'{ciphered_text}\'')
    print(f'Converted + Shifted [{shift_key}] text: \'{cipher.shift_text(ciphered_text, shift_key)}\'')

    enter_continue()


def decrypt() -> None:
    pass

def help() -> None:
    pass

def tests() -> None:
    pass

def quit() -> None:
    clear()
    sys.exit()


# All menu options dictionary
menu_options: dict = {
    0 : ('Encrypt', encrypt),
    1 : ('Decrypt', decrypt),
    2 : ('Help', help),
    3 : ('Tests', tests),
    4 : ('Quit', quit),
}


# Program functions
def print_options(options: dict) -> None:
    # Print all options with numbers
    for op, i in zip(options, range(len(options))):
        print(f'{i + 1}. {options[i][0]}')


def main(options: dict = menu_options) -> None:

    while(True):
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
    main()