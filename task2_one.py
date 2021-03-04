"""
    Title:      'Task 2' - Shift text with key (One file)
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
    Updated:    4/3/2021
"""

import re

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



def main() -> None:
    # Ask for user text to shift and the shift key
    to_cipher: str = input('Enter text: ')
    shift_key: str = input(f'Enter a shift key (Default {DEFAULT_KEY}): ')

    # Check cipher is empty, set default value
    if len(to_cipher) == 0:
        to_cipher = DEFAULT_TEXT

    # Validate text for conversion to int
    try:
        shift_key: int = int(shift_key) if len(shift_key) > 0 else DEFAULT_KEY
    except (TypeError, ValueError):
        # Use a default key
        shift_key: int = DEFAULT_KEY
    
    # Show original text and the shifted version (with key)
    print(f'Original text: \'{to_cipher}\'')
    print(f'Shifted [{shift_key}] text: \'{shift_text(convert_text(to_cipher), shift_key)}\'', end='\n\n')

    # Run all our test cases
    run_test_cases(TestType.CONVERTED, 'Converted')
    run_test_cases(TestType.SHIFTED, 'Shifted')


# Entry point
if __name__ == '__main__':
    main()