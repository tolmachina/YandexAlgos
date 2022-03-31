def inp_data():
    
    houses_and_money = list(map(int, input().split()))
    
    house_prices = list(map(int, input().split()))
    return houses_and_money[1], house_prices

def algosses(budget, houses):
    houses.sort()
    house_num = 0
    for house in houses:
        if house <= budget:
            budget -= house
            house_num += 1
        else:
            break
    return house_num

budget, houses = inp_data()

print(algosses(budget,houses))