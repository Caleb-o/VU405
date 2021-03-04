"""
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
    Updated:    4/3/2021
"""

import re

FROM_ALPHA: int = 26
FROM_A: int = 65

def convert_text(string: str) -> str:
    """
        Converts text to upper-case, removing whitespace and 
        replacing a special character (eg. '.') into an 'X'.
        
        Returns the converted string.
    """

    # Regular expression pattern to remove numbers and spaces
    return re.sub(r'[^A-Za-z]+|[0-9]+|\s+', '', string.replace('.', 'X')).upper()


def shift_text(string: str, key: int) -> str:
    return ''.join(chr((((ord(t) + key) - FROM_A) % FROM_ALPHA) + FROM_A) for t in convert_text(string))