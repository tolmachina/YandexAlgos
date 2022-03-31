def get_longest_word(line: str) -> str:
    long_word = ""
    for i in range(len(line)):
        if len(line[i]) > len(long_word):
            long_word = line[i]
    return long_word

def read_input() -> str:
    _ = input()
    line = input().strip().split()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
