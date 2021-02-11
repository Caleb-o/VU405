"""
    Title:      'Task 2' - Shift text with key
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
"""

import cipher, testing, sys

def main() -> None:
    """
        Main method to call test cases and user input to convert text.
    """
    testing.run_test_cases()
    
    # Run input unless an argument is provided
    ciphered_text: str = cipher.convert_text(input('\nEnter text: ')) if len(sys.argv) == 1 else sys.argv[1]
    print(f'Converted text: \'{cipher.shift_text(ciphered_text)}\'')


# Entry point
if __name__ == '__main__':
    main()