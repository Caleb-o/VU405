"""
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import term, cipher, sort


class TestType:
    CONVERTED = 0,
    SHIFTED = 1


# Cases - list of tuples with test case and expected output.
test_cases_convert: list = [ 
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

# Work with shift count of 1
test_cases_shifted: list = [
    ('abcd','DEFG', 3),
    ('hello.i.am.caleb','KHOORALADPAFDOHE', 3),
    ('KHOORALADPAFDOHE', 'HELLOXIXAMXCALEB', -3),
    ('Wh@1 @ Fin3 d4y t0d4y!?, h0w 4r3 y0u 2?.', 'JUSVAQLGQLUJELHK', 13),
    ('2021 1s th3 y34r 0f w1nn1ng!...345y', 'UVJATHYPPPIZZZA', 2)
]


def countUpper(string: str) -> int:
    count: int = 0

    for ch in string:
        if 'A' <= ch <= 'Z':
            count += 1
    return count


def testUppercase(string: str) -> None:
    print(f'{countUpper(string)} capitals in \'{string}\'')


def testBubbleSort() -> None:
    li: list = [2, 1, 7, 10, 3, 4, 9, 5, 6]
    sort.bubbleSort(li)
    print(li)


def run_test_cases(type: TestType, title: str = '') -> None:
    """
        Automated method of running tests. Uses 'test_cases' list.

        Returns None/void.
    """

    test_cases: list

    if (type == TestType.CONVERTED):
        test_cases = test_cases_convert
    elif (type == TestType.SHIFTED):
        test_cases = test_cases_shifted

    if (len(title) > 0):
        print(f'[{title}] ', end='')
    print(f'Running {term.tcol.PASS}{len(test_cases)}{term.tcol.TEXT} test cases...')

    pass_count: int = 0

    # Run through all cases using tuple and index
    for test, i in zip(test_cases, range(len(test_cases))):
        
        if (type == TestType.CONVERTED):
            case, expected = test
            interpreted = cipher.convert_text(case) 
        elif (type == TestType.SHIFTED):
            case, expected, key = test
            interpreted = cipher.shift_text(case, key)


        passed: bool = interpreted == expected
        passed_text: str = f'{term.tcol.PASS}PASSED{term.tcol.TEXT}' if passed else f'{term.tcol.FAIL}FAILED{term.tcol.TEXT}'

        if passed: pass_count += 1

        print(f'Test #{i+1}: {passed_text} - output \'{interpreted}\'', end='\n' if passed else f' - expected \'{expected}\'\n')
    
    # Show user number of tests passed and failed
    print(f'Passed {term.tcol.PASS if pass_count > 0 else term.tcol.FAIL}{pass_count}/{len(test_cases)}{term.tcol.TEXT} cases!', end='\n\n')