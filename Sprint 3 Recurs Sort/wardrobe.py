"""
inputs: - number of items
        - array with colours of each item [0,1,2]
output: - sort the array and stdout it
algo:
https://practicum.yandex.ru/learn/algorithms/courses/7f101a83-9539-4599-b6e8-8645c3f31fad/sprints/18167/topics/4a0eb007-5d71-4dda-bc54-df8c743f80ea/lessons/b0c6efdd-75f1-4fba-aa36-1746380e9b63/
"""

def count_sort(wardrobe: str):
    colours = [0,0,0]
    for item in wardrobe:
        if item == '0':
            colours[0] += 1
        elif item =='1':
            colours[1] += 1
        else:
            colours[2] += 1

    wardrobe = ['0'] * colours[0] + ['1'] * colours[1] + ['2'] * colours[2]
    return wardrobe

n = input()
wardrobe = input().split()

print(' '.join(count_sort(wardrobe))) 