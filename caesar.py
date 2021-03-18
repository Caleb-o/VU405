"""
    Title:      'Task 3' - Convert and shift text with key - user program
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
    Updated:    18/3/2021
"""

import re, sys, os, time

# Conversion constants
FROM_ALPHA: int = 26
FROM_A: int = 65


# Main defaults
DEFAULT_TEXT: str = 'Hello.World!23    @.'
DEFAULT_KEY: int = 3


def convert_text(string: str) -> str:
    """
        Converts text to upper-case, removing whitespace and 
        replacing a special character (eg. '.') into an 'X'.
        
        Returns the converted string.
    """

    # Regular expression pattern to remove numbers and spaces
    return re.sub(r'[^A-Za-z]+|[0-9]+|\s+', '', string.replace('.', 'X')).upper()


def shift_text(string: str, key: int, convert: bool = True) -> str:
    """
        Shifts each character by key value. Optional value
        for converting prior to shift.
    """
    shifted_str: str = ''
    
    for t in convert_text(string) if convert else string:
        shifted_str += chr((((ord(t) + key) - FROM_A) % FROM_ALPHA) + FROM_A)
    return shifted_str


# Testing enum
class TestType:
    CONVERTED = 0,
    SHIFTED = 1


# Colours for terminal output (Test cases)
class tcol:
    TEXT = '\033[0m' # White
    PASS = '\033[92m' # Green
    FAIL = '\033[91m' # Red


# Cases - list of tuples with test case and expected output.
test_cases_convert: list = [ 
    ('13129828^#^@^hello,&@#&&#@world!848($@(','HELLOWORLD'),
    ('My name is Caleb', 'MYNAMEISCALEB'),
    ('Hello.my.name.is.johnny.', 'HELLOXMYXNAMEXISXJOHNNYX'),
    ('@What29is&your*name?.', 'WHATISYOURNAMEX'),
    ('    ArE*&we88282he?re?.','AREWEHEREX'),
    ('2021', ''),
    ('&$@&*$.@($*!$^)!^', 'X'),
    ('                       a.b.c                  ', 'AXBXC'),
    ('@A!b#C%d^E&f*G(h)I', 'ABCDEFGHI'),
    ('......@#$%^&......', 'XXXXXXXXXXXX'),
]

test_cases_shifted: list = [
    ('hello.i.am.caleb','KHOORALADPAFDOHE', 3),
    ('KHOORALADPAFDOHE', 'HELLOXIXAMXCALEB', -3),
    ('Wh@1 @ Fin3 d4y t0d4y!?, h0w 4r3 y0u 2?.', 'JUSVAQLGQLUJELHK', 13),
    ('2021 1s th3 y34r 0f w1nn1ng!...345y', 'UVJATHYPPPIZZZA', 2),
    ('   .4.    .3.    .2021.    ', 'AAAAAA', 3),
    ('WHATISYOURNAMEX', 'EPIBQAGWCZVIUMF', 8),
    ('EPIBQAGWCZVIUMF', 'WHATISYOURNAMEX', -8),
    ('I am coding in Python...But I prefer programming in C.', 'YQCSETYDWYDFOJXEDNNNRKJYFHUVUHFHEWHQCCYDWYDSN', 16),
    ('YQCSETYDWYDFOJXEDNNNRKJYFHUVUHFHEWHQCCYDWYDSN', 'IAMCODINGINPYTHONXXXBUTIPREFERPROGRAMMINGINCX', -16),
    ('L00king 1nt0..@5tud1ng.@?4..0d1pl0m48280f   50ftw4r3 d3v.2021.', 'GFDIBIOSSOPYIBSSSYKGHAAORMYQSS', 255),
]


def run_test_cases(type: TestType, title: str = '') -> None:
    """
        Automated method of running tests. Uses 'test_cases' list.

        Returns None/void.
    """

    test_cases: list

    if (type == TestType.CONVERTED):
        test_cases = test_cases_convert
    elif (type == TestType.SHIFTED):
        test_cases = test_cases_shifted

    if (len(title) > 0):
        print(f'[{title}] ', end='')
    print(f'Running {tcol.PASS}{len(test_cases)}{tcol.TEXT} test cases...')

    pass_count: int = 0

    # Run through all cases using tuple and index
    for test, i in zip(test_cases, range(len(test_cases))):
        
        if (type == TestType.CONVERTED):
            case, expected = test
            interpreted = convert_text(case) 
        elif (type == TestType.SHIFTED):
            case, expected, key = test
            interpreted = shift_text(case, key)


        passed: bool = interpreted == expected
        passed_text: str = f'{tcol.PASS}PASSED{tcol.TEXT}' if passed else f'{tcol.FAIL}FAILED{tcol.TEXT}'

        if passed: pass_count += 1

        print(f'Test #{i+1}: {passed_text} - output \'{interpreted}\'', end='\n' if passed else f' - expected \'{expected}\'\n')
    
    # Show user number of tests passed and failed
    print(f'Passed {tcol.PASS if pass_count > 0 else tcol.FAIL}{pass_count}/{len(test_cases)}{tcol.TEXT} cases!', end='\n\n')

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
    ciphered_text: str = convert_text(to_encrypt)
    
    print(f'Original text: \'{to_encrypt}\'')
    print(f'Encrypted [{shift_key}] text: \'{shift_text(ciphered_text, shift_key)}\'')


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
    ciphered_text: str = convert_text(to_decrypt)
    
    print(f'Original text: \'{to_decrypt}\'')
    print(f'Decrypted [{shift_key}] text: \'{shift_text(ciphered_text, shift_key)}\'')


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
    print("""
Encrypt - Asks for a message and key to encrypt and shows the encrypted text.
Decrypt - Asks for an encrypted message and key to decrypt and shows the decrypted text.
Tests - Shows test cases, whether conversion and full encryption passes the test.
Quit - Exits the program.
""")
    enter_continue()


def opt_tests() -> None:
    """
        Runs all the test cases to date.
    """
    run_test_cases(TestType.CONVERTED, 'Converted')
    run_test_cases(TestType.SHIFTED, 'Shifted')
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
    3 : ('Unit Tests', opt_tests),
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

        inp = input('\nOption> ')

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
            time.sleep(REST_TIME)


# Entry point
if __name__ == '__main__':
    # Command line usage
    if len(sys.argv) > 1:
        # Check if arguments are correct length 
        if len(sys.argv) < 3:
            print('Command syntax: caesar.py [type: -e -d] [message] [key] OR caesar.py for UI.\neg. task3.py -e "hello" 3')
        else:
            cmd = cli_options[sys.argv[1]](sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else DEFAULT_KEY)
    else:
        # Call UI program
        main()