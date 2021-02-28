"""
    Title:      'Task 1' - Main
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import cipher, testing, sys

def main() -> None:
    """
        Main method to call test cases and user input to convert text.
    """
    # Run input unless an argument is provided
    print('Converted text: \'' + cipher.convert_text(input('\nEnter text: ') if len(sys.argv) == 1 else sys.argv[1]) + '\'')

    testing.run_test_cases(testing.TestType.CONVERTED, 'Converted')


# Entry point
if __name__ == '__main__':
    main()