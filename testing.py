"""
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import term
import cipher

# Cases - list of tuples with test case and expected output.
test_cases: list = [ 
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


def countUpper(string: str) -> int:
    count: int = 0

    for ch in string:
        if 'A' <= ch <= 'Z':
            count += 1
    return count


def testUppercase(string: str) -> None:
    print(f'{countUpper(string)} capitals in \'{string}\'')


def run_test_cases() -> None:
    """
        Automated method of running tests. Uses 'test_cases' list.

        Returns None/void.
    """

    print(f'Running {term.tcol.PASS}{len(test_cases)}{term.tcol.TEXT} test cases...')

    pass_count: int = 0

    # Run through all cases using tuple and index
    for test, i in zip(test_cases, range(len(test_cases))):
        case, expected = test

        interpreted: str = cipher.convert_text(case)
        passed: bool = interpreted == expected
        passed_text: str = f'{term.tcol.PASS}PASSED{term.tcol.TEXT}' if passed else f'{term.tcol.FAIL}FAILED{term.tcol.TEXT}'

        if passed: pass_count += 1

        print(f'Test #{i}: {passed_text} - output \'{interpreted}\'', end='\n' if passed else f' - expected \'{expected}\'\n')
    
    # Show user number of tests passed and failed
    print(f'Passed {term.tcol.PASS if pass_count > 0 else term.tcol.FAIL}{pass_count}/{len(test_cases)}{term.tcol.TEXT} cases!')