"""
gen_brackets(n)
inp: ni0...10
out: alphabetically print all combinations of parentheses of Length 2 n,
"""

def get_brackets(n, brackets, left,right):
    if n == 0:
        print(brackets)
    else:
        if len(brackets) == 0:
            get_brackets(n-1, brackets + '(',left -1,right)
        elif n == 1:
            get_brackets(n-1,brackets + ')',left,right-1)
        elif right == left:
            get_brackets(n-1,brackets + '(',left-1,right)
        elif left == 0:
            get_brackets(n-1,brackets + ')',left,right-1)
        else:
            get_brackets(n-1, brackets + '(',left-1,right)
            get_brackets(n-1,brackets + ')',left,right-1)


n = int(input())
brackets = ""
get_brackets(2*n, brackets, n, n)
