import re

def onlydigits(text: str) -> str:
    return re.sub(r'[A-Za-z]+|\s', '', text)

print('Digits: ', onlydigits(input('Enter text: ')))