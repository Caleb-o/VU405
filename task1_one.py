"""
    Title:      'Task 1' - Main
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import re, sys


def convert_to_Caesar(string: str) -> str:
    """
        Converts text to upper-case, removing whitespace and 
        replacing a special character (eg. '.') into an 'X'.
        
        Returns the converted string.
    """

    # Regular expression pattern to remove numbers and spaces
    return re.sub(r'[^A-Za-z]+|[0-9]+|\s+', '', string.replace('.', 'X').upper())


def run_test_cases():
    # Test 1
    result = convert_to_Caesar('13129828^#^@^hello,&@#&&#@world!848($@(')
    if (result == 'HELLOWORLD'):
        print('Test 1 OK')
    else:
        print('Test 1 error: ' + result)

    # Test 2
    result = convert_to_Caesar('My name is Caleb')
    if (result == 'MYNAMEISCALEB'):
        print('Test 2 OK')
    else:
        print('Test 2 error: ' + result)

    # Test 3
    result = convert_to_Caesar('Hello.my.name.is.johnny.')
    if (result == 'HELLOXMYXNAMEXISXJOHNNYX'):
        print('Test 3 OK')
    else:
        print('Test 3 error: ' + result)

    # Test 4
    result = convert_to_Caesar('@What29is&your*name?.')
    if (result == 'WHATISYOURNAMEX'):
        print('Test 4 OK')
    else:
        print('Test 4 error: ' + result)

    # Test 5
    result = convert_to_Caesar('    ArE*&we88282he?re?.')
    if (result == 'AREWEHEREX'):
        print('Test 5 OK')
    else:
        print('Test 5 error: ' + result)

    # Test 6
    result = convert_to_Caesar('2021')
    if (result == ''):
        print('Test 6 OK')
    else:
        print('Test 6 error: ' + result)

    # Test 7
    result = convert_to_Caesar('&$@&*$.@($*!$^)!^')
    if (result == 'X'):
        print('Test 7 OK')
    else:
        print('Test 7 error: ' + result)

    # Test 8
    result = convert_to_Caesar('                       a.b.c                  ')
    if (result == 'AXBXC'):
        print('Test 8 OK')
    else:
        print('Test 8 error: ' + result)

    # Test 9
    result = convert_to_Caesar('@A!b#C%d^E&f*G(h)I')
    if (result == 'ABCDEFGHI'):
        print('Test 9 OK')
    else:
        print('Test 9 error: ' + result)

    # Test 10
    result = convert_to_Caesar('......@#$%^&......')
    if (result == 'XXXXXXXXXXXX'):
        print('Test 10 OK')
    else:
        print('Test 10 error: ' + result)


def main():
    run_test_cases()
    print('Converted text: \'' + convert_to_Caesar(input('\nEnter text: ') if len(sys.argv) == 1 else sys.argv[1]) + '\'')


# Entry
main()