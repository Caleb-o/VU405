"""
    Title:      'Task 1' - Main
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import cipher, testing

def main() -> None:
    """
        Main method to call test cases and user input to convert text.
    """
    testing.run_test_cases()
    
    print('Converted text: \'' + cipher.convert_text(input('\nEnter text: ')) + '\'')


# Entry point
if __name__ == '__main__':
    main()