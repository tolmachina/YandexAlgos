"""
[1,2,3,4,4,4,6,12]
price of bike is 4.
we need to get indexes of price, which is 2 and 2x price which is 6.
we use binary search as an array sorted.
how to search for 2 variables in binary search?
Or just search twice?
"""

def two_bikes_wrap(money,left,right,bike):
	min_day = -2
	def two_bikes(money, left, right, bike, min_day):
		if left >= right:
			return min_day
		mid = (right+left)// 2
		if bike <= money[mid]:
			min_day = mid
			return two_bikes(money,left, mid, bike, min_day)
		else:
			return two_bikes(money,mid+1,right,bike, min_day)
	return two_bikes(money,left,right,bike,min_day)


def main():
	n=input()
	money = list(map(int, input().split()))
	bike = int(input())

	day_of_first_purchase = two_bikes_wrap(money,0,len(money), bike) + 1
	day_of_last_purchase = two_bikes_wrap(money,0,len(money), bike * 2) + 1
	print(day_of_first_purchase, day_of_last_purchase)


if __name__ == '__main__':
	main()
