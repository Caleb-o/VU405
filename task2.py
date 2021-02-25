"""
    Title:      'Task 2' - Shift text with key
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
"""

import cipher, testing, sys


def main() -> None:
    testing.run_test_cases(testing.TestType.SHIFTED, 'Shifted')

    shift_key: int = 3
    to_cipher: str = input('\nEnter text: ')
    
    print(f'Original text: \'{to_cipher}\'')
    print(f'Shifted [{shift_key}] text: \'{cipher.shift_text(cipher.convert_text(to_cipher), shift_key)}\'')


# Entry point
if __name__ == '__main__':
    main()