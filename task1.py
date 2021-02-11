"""
    Title:      'Task 1' - Main
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import cipher, testing, sys, sort

def main() -> None:
    """
        Main method to call test cases and user input to convert text.
    """
    testing.run_test_cases()
    
    # Run input unless an argument is provided
    print('Converted text: \'' + cipher.convert_text(input('\nEnter text: ') if len(sys.argv) == 1 else sys.argv[1]) + '\'')


# Entry point
if __name__ == '__main__':
    main()