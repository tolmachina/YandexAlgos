from typing import Tuple
from collections import Counter

def get_excessive_letter(shorter: str, longer: str) -> str:
    # Здесь реализация вашего решения
    long_dct, shrt_dct = {}, {}
    for let in longer:
        long_dct[let] = long_dct.get(let,0) + 1
    
    for letter in shorter:
        shrt_dct[letter] = shrt_dct.get(letter,0) + 1
    
    for key in long_dct:
        if key not in shrt_dct:
            return key
        if shrt_dct[key] < long_dct[key]:
            return key
        
def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
