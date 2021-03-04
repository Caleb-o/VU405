"""
    Title:      'Task 2' - Shift text with key
    Author:     Caleb Otto-Hayes
    Date:       11/2/2021
    Updated:    4/3/2021
"""

import cipher, testing


def main() -> None:
    # Ask for user text to shift and the shift key
    to_cipher: str = input('Enter text: ')
    shift_key: str = input('Enter a shift key: ')

    # Validate text for conversion to int
    try:
        shift_key: int = int(shift_key) if len(shift_key) > 0 else 3
    except (TypeError, ValueError):
        shift_key: int = 3
    
    print(f'Original text: \'{to_cipher}\'')
    print(f'Shifted [{shift_key}] text: \'{cipher.shift_text(cipher.convert_text(to_cipher), shift_key)}\'', end='\n\n')

    # Run all our test cases
    testing.run_test_cases(testing.TestType.CONVERTED, 'Converted')
    testing.run_test_cases(testing.TestType.SHIFTED, 'Shifted')


# Entry point
if __name__ == '__main__':
    main()