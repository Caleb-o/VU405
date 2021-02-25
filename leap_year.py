years: list = [
    1900,
    2000,
    2003,
    2004,
    2012,
    2017,
    2020,
    2024,
    2028,
]

def is_leap_year(year: int) -> bool:
    return all(year % n == 0 for n in (4, 100, 400))


def test_years() -> None:
    for year in years:
        text: str = 'is a leap year' if is_leap_year(year) else 'is not a leap year'
        print(f'{year} {text}')


if __name__ == '__main__':
    test_years()