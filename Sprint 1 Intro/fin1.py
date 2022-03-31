"""
ID 61706117
"""


def get_nulls_positions(street):
    """
    gets indexes of nulls in array
    """
    nulls = []
    for i in range(len(street)):
        if street[i] == 0:
            nulls.append(i)
    return nulls


def dist_to_null(street):
    """
    Adding distances to array distances in three parts:
    1. From beginning of array up to first null occurrence
    2. From first null iterating till last null.
    3 From last null till end of array
    Returning distances
    """
    nulls = get_nulls_positions(street)
    distances = []
    first_null = nulls[0]
    last_null = nulls[-1]
    # fill up to first_null zero
    for y in range(first_null):
        distance = abs(first_null - y)
        distances.append(distance)
    # fill the middle
    for j in range(0, len(nulls)-1):
        start_null = nulls[j]
        end_null = nulls[j+1]
        for q in range(start_null, end_null):
            distance = min(abs(start_null - q), abs(end_null - q))
            distances.append(distance)
    # fill from last zero till end of array
    for d in range(0, len(street)-last_null):
        if len(street) - last_null == 1:
            distances.append(0)
        else:
            distances.append(d)
    return distances


def main():
    length_of_street = input()
    street_nums = input()
    street = list(map(int, street_nums.split()))
    print(*dist_to_null(street))


if __name__ == '__main__':
    main()
