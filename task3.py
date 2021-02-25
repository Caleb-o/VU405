"""
    Title:      'Task 3' - Convert and shift text with key
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
"""

import cipher, testing, sys

def main() -> None:
    """
        Main method to call test cases and user input to convert text.
    """
    testing.run_test_cases(testing.TestType.CONVERTED, 'Converted')
    testing.run_test_cases(testing.TestType.SHIFTED, 'Shifted')
    testing.run_test_cases(testing.TestType.BOTH, 'Converted + Shifted')

    argc: int = len(sys.argv)
    shift_key: int = 1 if argc <= 2 else int(sys.argv[2])
    to_cipher: str = input('\nEnter text: ') if argc == 1 else sys.argv[1]
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(to_cipher)
    
    print(f'Original text: \'{to_cipher}\'')
    print(f'Converted text: \'{ciphered_text}\'')
    print(f'Shifted [{shift_key}] text: \'{cipher.shift_text(to_cipher, shift_key)}\'')
    print(f'Converted + Shifted [{shift_key}] text: \'{cipher.shift_text(ciphered_text, shift_key)}\'')


# Entry point
if __name__ == '__main__':
    main()