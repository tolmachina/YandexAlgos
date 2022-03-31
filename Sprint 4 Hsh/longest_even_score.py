# from tabnanny import check



def get_longest(scores):
    
    max_lenght = 0
    
    total = 0
    sum_up_to_position = {}

    for i in range(len(scores)):
        
        if scores[i] == 0:
            total -= 1
        else: total += 1

        if total == 0:
            cur_lenght = i + 1
            if cur_lenght > max_lenght:
                max_lenght = cur_lenght
        else:
            if total not in sum_up_to_position:
                sum_up_to_position[total] = i + 1
            else:
                cur_lenght = (i + 1 - sum_up_to_position[total])
                if cur_lenght > max_lenght:
                    max_lenght = cur_lenght

    return max_lenght


# assert (get_longest([0]) == 0)
# assert (get_longest([1]) == 0)
# assert (get_longest([0,1]) == 2)
# assert (get_longest([1,0]) == 2)
# assert (get_longest([1,0,0]) == 2)
# assert (get_longest([1,0,0,1]) == 4)
# assert (get_longest([1,0,0,1,0,1]) == 6)
# assert (get_longest([0,1,1,1,0,1,0]) == 4)
# assert (get_longest([0,1,0]) == 4)



n = int(input())
if n == 0:
    print(0)
else:
    stringy = input()
    scores = list(map(int, stringy.split()))
    print(get_longest(scores))

