from typing import Tuple
def sum_two_binary(num1: str,num2: str) -> str:

	top = num1 if len(num1) > len(num2) else num2
	bottom = num1 if (num1 != top) else num2
	result = ""
	delta = len(top)-len(bottom)
	cache = 0
	for i in range(len(bottom)-1,-1,-1):
		if top[i+delta]=="1" and bottom[i] == "1":
			if cache == 1: result += "1"
			else: result += "0"
			cache = 1
		elif (top[i+delta]=="1" or bottom[i]=="1"):
			if cache == 1: result += "0"
			elif cache == 0: result += "1"
		elif top[i+delta] == "0" and bottom[i] == "0":
			if cache == 1:
				result += "1"
				cache = 0
			else:
				result += "0"
	if len(top) == len(bottom):
		if cache == 1:
			result += "1"
		return result[::-1]
	else:
		for j in range(delta-1,-1, -1):
			if cache == 0:
				result += top[j]
			else:
				if top[j] == "1":
					result += "0"
				else: 
					result += "1"
					cache = 0
		if cache == 1:
			result += "1"

		return result[::-1]
		
num1 = input().strip()
num2 = input().strip()
print(sum_two_binary(num1,num2))

