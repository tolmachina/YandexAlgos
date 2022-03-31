# def outer_func(x):
#     y = 4
#     return lambda z: x + y + z

# i = 2
# closure = outer_func(x=i)
# print(f"closure({i+5}) = {closure(z=i+5)}")


# def outer_func(x):
#     y = 4
#     def inner_func(z):
#         print(f"x = {x}, y = {y}, z = {z}")
#         return x + y + z
#     return inner_func
 
# closure = outer_func(x=3)

# print(closure(z=5))


def wrap(number,query):
    def binary_search(keys, query):
        min_ind = 0
        max_ind = len(keys) - 1
        while min_ind <= max_ind:
            mid_ind = int((min_ind + max_ind)/2)
            if query == keys[mid_ind]:
                return mid_ind
            elif query > keys[mid_ind]:
                min_ind = mid_ind + 1
            else:
                max_ind = mid_ind - 1
        return -1

    
    foo = binary_search(number,query)
    print(foo)
    return foo

number = [5,6,7,1,2,3,4]
query = 4

print("wtf ==", wrap(number, query))
