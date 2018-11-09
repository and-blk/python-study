#!/usr/bin/python3

equal = "="
space = " "
i = 0
while i < 40 :
	i = i + 1
	print(space * (40 - i), equal * i, equal * i)

	if i == 50:
		break
		print("i is equals 50")
else:
	print("i wasn't equals 50")