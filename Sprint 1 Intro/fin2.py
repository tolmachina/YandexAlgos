"""
ID 61706127
"""


def game(k, dict_numb):
    """
    iterating in time t from 1 to 9 inclusive.
    """
    score = 0
    for t in range(1, 10):
        if t in dict_numb:
            if dict_numb[t] <= k*2:
                score += 1                
    return score


def get_data():
    """
    reads data into dictionary with numbers counts.
    """
    buttons = int(input())
    dict_numb = {}
    for i in range(4):
        line = [int(char) if char != "." else 0 for char in input()]
        for char in line:
            dict_numb[char] = dict_numb.get(char, 0) + 1
    return buttons, dict_numb


def main():
    buttons, dict_numb = get_data()
    print(game(buttons, dict_numb))


if __name__ == '__main__':
    main()
